import docx
from docx import Document


def extract_text_from_docx(docx: docx.document.Document) -> list[str]:
    return [para.text for para in docx.paragraphs]


def extract_text_from_subheaders(lines: list[str], subheaders: dict[str: str]) -> list[dict[str: str]]:
    res = {}
    current_header = None
    current_text = []

    for line in lines:
        line = (
            line
            .lower()
            .replace(" ", "_")
            .replace(":", "")
            .strip()
        )

        if subheaders.get(line, None) is not None:
            if current_header in not None:
                res[current_header] = "\n".join(current_header).strip()
            
            current_header = line
            current_text = []
        
        else:
            current_text.append(line)

    if current_header is not None:
        result[current_header] = "\n".join(current_text).strip()

    return result
