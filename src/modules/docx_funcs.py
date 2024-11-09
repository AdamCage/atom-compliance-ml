from pathlib import Path
import re
from typing import Any, List, Dict

import docx
from docx import Document


def extract_text_from_docx(docx: docx.document.Document) -> List[str]:
    return [para.text for para in docx.paragraphs]


def extract_elements(lines: List[str], subheader: str) -> str:
    result = []
    start_found = False

    for i, element in enumerate(lines):
        if not start_found and element.lower().strip().replace(" ", "_").startswith(subheader):
            start_found = True
            result.append(element)
            continue

        if start_found:
            if ':' in element:
                break
            result.append(element)

    return "\n".join(result)


def create_ds_row(fid: str, hmi_dir: Path, ssts_dir: Path, columns: List[str]) -> Dict[str, Any]:
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

        row = dict().fromkeys(columns)

        row["id"] = fid
        row["case_name"] = re.sub(r"\[I-\d+\]", "", re.sub(r'\$\$.*?\$\$|\s*[\xa0]+\s*', ' ', hmi_docx.paragraphs[0].text)).strip()
        row["full_uc_text"] = "\n".join(uc_lines)
        row["full_ssts_text"] = "\n".join(extract_text_from_docx(ssts_docx)) if ssts_docx is not None else None
        row["main_scenario"] = extract_elements(uc_lines, "main_scenario")
        row["goal"] = extract_elements(uc_lines, "goal")
        row["preconditions"] = extract_elements(uc_lines, "preconditions")
        row["postconditions"] = extract_elements(uc_lines, "postconditions")
        row["other"] = (
            extract_elements(uc_lines, "description")
            + extract_elements(uc_lines, "scope")
            + extract_elements(uc_lines, "actors")
            + extract_elements(uc_lines, "requirements")
            + extract_elements(uc_lines, "trigger")
            + extract_elements(uc_lines, "use_case_title")
            + extract_elements(uc_lines, "tigger")
            + extract_elements(uc_lines, "components")
            + extract_elements(uc_lines, "function_logic")
            + extract_elements(uc_lines, "additional_info")
            + extract_elements(uc_lines, "display")
            + extract_elements(uc_lines, "notification")
            + extract_elements(uc_lines, "use_case")
            + extract_elements(uc_lines, "triggers")
            + extract_elements(uc_lines, "requirenments")
        )
        row["alternative_scenario"] = (
            extract_elements(uc_lines, "alternative_scenario_a")
            + extract_elements(uc_lines, "alternative_scenario_b")
            + extract_elements(uc_lines, "alternative_scenario_c")
            + extract_elements(uc_lines, "alternative_scenario")
            + extract_elements(uc_lines, "alternative_scenarios")
            + extract_elements(uc_lines, "alternative_scenario_a_a(turn_off_the_hotspot)")
        )

        row["differences"] = None
        row["descriptions"] = None
        row["complience_level"] = None

    return row
