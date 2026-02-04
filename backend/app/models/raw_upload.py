import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class RawUpload(Base):
    __tablename__ = "raw_uploads"

    upload_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String, nullable=False)
    company_id = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    status = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
