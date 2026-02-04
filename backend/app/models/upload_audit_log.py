import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class UploadAuditLog(Base):
    __tablename__ = "upload_audit_logs"

    audit_id = Column(String, primary_key=True)
    upload_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
