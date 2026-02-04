from app.parsers.tally_xml_parser import parse_tally_xml


def parse_raw_file(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        xml_content = f.read()

    return parse_tally_xml(xml_content)
