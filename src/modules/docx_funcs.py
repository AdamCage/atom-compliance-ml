from pathlib import Path
import re
from typing import Any

import docx
from docx import Document


def extract_text_from_docx(docx: docx.document.Document) -> list[str]:
    return [para.text for para in docx.paragraphs]


def extract_text_from_subheaders(lines: list[str], subheaders: dict[str: str]) -> list[dict[str: str]]:
    res = {}
    current_header = None
    current_text = []

    for line in lines:
        line_ = (
            line
            .replace("\\n", "")
            .strip()
            .lower()
            .replace(" ", "_")
        )
        line_ = re.sub(":.*", "", line_)

        if subheaders.get(line_, None) is not None:
            if current_header is not None:
                res[current_header] = "\n".join(current_text).strip()
            
            current_header = line
            current_text = []
        
        else:
            current_text.append(line)

    if current_header is not None:
        res[current_header] = "\n".join(current_text).strip()

    return res


def extract_text_from_subheader(lines: list[str], subheader: str) -> list[str]:
    res = {}

    flat_lines = "\n".join(lines)
    pattern = rf'{re.escape(subheader)}(.*?)(?=:?\n.*?:?\n)'

    match = re.search(pattern, flat_lines, re.DOTALL)

    if match:
        return match.group(1).strip()
    
    else:
        return "NO DATA"


def create_ds_row(fid: str, hmi_dir: Path, ssts_dir: Path, columns: list[str], hmi_subheaders) -> dict[str: Any]:
    try:
        hmi_docx = Document(hmi_dir / f'UC-{fid}.docx')
    
    except Exception as e:
        print(f'Warning! {e}')
        hmi_docx = None

    try:
        ssts_docx = Document(ssts_dir / f'SSTS-{fid}.docx')
    
    except Exception as e:
        print(f'Warning! {e}')
        ssts_docx = None

    row = dict().fromkeys(columns)

    if hmi_docx is not None:
        uc_lines = extract_text_from_docx(hmi_docx)
        subheaders_texts = extract_text_from_subheaders(uc_lines, hmi_subheaders)
        subheaders_texts = {k.lower().replace(" ", "_").replace(":", "").strip(): v for k, v in subheaders_texts.items()}

        row = dict().fromkeys(columns)

        row["id"] = fid
        row["case_name"] = re.sub("\[I-\d+\]", "", re.sub(r'$$.*?$$|\s*[\xa0]+\s*', ' ', hmi_docx.paragraphs[0].text)).strip()
        row["full_uc_text"] = "\n".join(uc_lines)
        row["full_ssts_text"] = "\n".join(extract_text_from_docx(ssts_docx)) if ssts_docx is not None else None
        row["main_scenario"] = subheaders_texts.get("main_scenario", "")
        row["goal"] = subheaders_texts.get("goal", "")
        row["preconditions"] = subheaders_texts.get("preconditions", "")
        row["postconditions"] = subheaders_texts.get("postconditions", "")
        row["other"] = (
            subheaders_texts.get("description", "")
            + subheaders_texts.get("scope", "")
            + subheaders_texts.get("actors", "")
            + subheaders_texts.get("requirements", "")
            + subheaders_texts.get("trigger", "")
            + subheaders_texts.get("use_case_title", "")
            + subheaders_texts.get("tigger", "")
            + subheaders_texts.get("components", "")
            + subheaders_texts.get("function_logic", "")
            + subheaders_texts.get("additional_info", "")
            + subheaders_texts.get("display", "")
            + subheaders_texts.get("notification", "")
            + subheaders_texts.get("use_case", "")
            + subheaders_texts.get("triggers", "")
            + subheaders_texts.get("requirenments", "")
        )
        row["alternative_scenario"] = (
            subheaders_texts.get("alternative_scenario_a", "")
            + subheaders_texts.get("alternative_scenario_b", "")
            + subheaders_texts.get("alternative_scenario_c", "")
        )

        row["differences"] = None
        row["descriptions"] = None
        row["complience_level"] = None

    return row
