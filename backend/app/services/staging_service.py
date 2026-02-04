from app.models.staged_vouchers import StagedVoucher

def stage_vouchers(upload_id: str, vouchers: list[dict], db):
    for v in vouchers:
        record = StagedVoucher(
            upload_id=upload_id,
            voucher_no=v["voucher_no"],
            voucher_date=v["voucher_date"],
            amount=v["amount"],
        )
        db.add(record)

    db.commit()
