import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, Numeric
from app.db.base import Base

class StagedVoucher(Base):
    __tablename__ = "staged_vouchers"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    upload_id = Column(UUID(as_uuid=True), index=True)
    voucher_no = Column(String)
    voucher_date = Column(Date)
    amount = Column(Numeric)
