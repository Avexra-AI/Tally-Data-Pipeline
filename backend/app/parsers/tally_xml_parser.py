import xml.etree.ElementTree as ET

def parse_tally_xml(xml_content: str) -> list[dict]:
    root = ET.fromstring(xml_content)
    vouchers = []

    for v in root.findall(".//VOUCHER"):
        vouchers.append({
            "voucher_no": v.findtext("VOUCHERNUMBER"),
            "voucher_date": v.findtext("DATE"),
            "amount": v.findtext("AMOUNT"),
        })

    return vouchers
