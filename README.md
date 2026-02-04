# Phase 1 — Tally Data Ingestion

## Repo Structure

backend/
├── app/api/v1/ # FastAPI endpoints: ingest.py, health.py
├── core/ # Config and security
├── db/ # Database session, base, models
├── parsers/ # XML parsing logic
├── services/ # Parsing, staging, storage services
├── utils/ # Audit logging
├── main.py
└── requirements.txt
connector/
├── tally_connector.py
└── requirements.txt 
.gitignore

##  Phase 1 Goals

- Accept real Tally XML files  
- Upload via ingestion API  
- Store raw files safely (`backend/storage/raw/`)  
- Parse XML into staging tables  
- Provide upload confirmation and audit logging  

##  Phase 1 Deliverables

1. Connector v0  
2. Ingestion API  
3. Raw data storage  
4. Parsing & staging tables  
5. Upload status & audit logging  
6. Minimal verification endpoint  

## Phase 1 Execution

1. Ingestion API - `backend/app/api/v1/ingest.py`  
2. Raw storage - `backend/storage/raw/`  
3. Parsing - `backend/parsers/tally_xml_parser.py`  
4. Staging tables - `backend/db/models/`  
5. Connector v0 - `connector/tally_connector.py`  
6. End-to-end test - upload - parse - staging  

##  Notes

- Raw files are immutable 
- Parsing logic is separate from API routes  
- Phase 2 will add S3 storage and async processing

##  Success Criteria

- Upload returns `upload_id`  
- File appears in `backend/storage/raw/`  
- Entry exists in `raw_uploads` table  
- XML parsing completes without errors  
- `staged_vouchers` contains parsed rows
