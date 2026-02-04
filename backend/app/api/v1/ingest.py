import uuid
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.security import validate_connector_token
from app.db.session import get_db
from app.models.raw_upload import RawUpload
from app.services.storage_service import save_raw_file
from app.utils.audit_logger import log_audit

router = APIRouter(prefix="/ingest", tags=["Ingestion"])


@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    _: str = Depends(validate_connector_token),
):
    # Generate upload_id
    upload_id = (uuid.uuid4())

    # Save raw file to disk (immutable)
    storage_path = save_raw_file(upload_id, file)

    # Create raw_upload DB record
    raw_upload = RawUpload(
        upload_id=upload_id,
        tenant_id="default_tenant",
        company_id="default_company",
        file_name=file.filename,
        storage_path=storage_path,
        status="STORED",
    )

    db.add(raw_upload)
    db.commit()

    #  Write audit log
    log_audit(db, upload_id, "File received and stored successfully")

    # Return minimal response
    return {
        "upload_id": str(upload_id),
        "status": "STORED",
    }
