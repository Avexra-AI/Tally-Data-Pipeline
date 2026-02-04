import uuid
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.security import validate_connector_token
from app.db.session import get_db
from app.models.raw_upload import RawUpload
from app.services.storage_service import save_raw_file
from app.services.parse_service import parse_raw_file
from app.services.staging_service import stage_vouchers
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

    # Step 2: Save raw file to disk
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

    # Step 3: Parse raw XML (outside route logic)
    parsed_data = parse_raw_file(storage_path)

    # Step 4: Stage parsed output
    stage_vouchers(upload_id, parsed_data, db)


    # Audit log
    log_audit(db, upload_id, "File stored, parsed, and staged successfully")

    return {
        "upload_id": str(upload_id),
        "status": "STORED_AND_STAGED",
    }
