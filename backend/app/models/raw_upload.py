from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class RawUpload(Base):
    __tablename__ = "raw_uploads"

    upload_id = Column(String, primary_key=True)
    tenant_id = Column(String, nullable=False)
    company_id = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    status = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
