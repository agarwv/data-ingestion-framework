UPDATED

# Ingestion Framework

This repository supports ingestion from multiple sources:

- Oracle and MSSQL (via SQLAlchemy)
- File sources: CSV, XLS, XLSX
- SharePoint (via Graph API with certificate-based auth)

All data is loaded into a central MSSQL database.

## Structure
- `src/` - Core Python source files
- `config/` - Config JSONs for each ingestion entity
- `mappings/` - Mapping JSONs for data quality
- `logs/` - Log output folder

## How to Run
```bash
python main.py
```

## Extend
Add new JSON config files under `config/{source_type}/` and mapping files under `mappings/`.
