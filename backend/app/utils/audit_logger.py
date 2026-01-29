import uuid
from app.models.upload_audit_log import UploadAuditLog

def log_audit(db, upload_id: str, message: str):
    audit = UploadAuditLog(
        audit_id=str(uuid.uuid4()),
        upload_id=upload_id,
        message=message,
    )
    db.add(audit)
    db.commit()
