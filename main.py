
from src.ingestion_router import IngestionRouter
from src.logger import setup_logging

def main():
    logger = setup_logging()
    try:
        # Sample usage for different entity configs
        for config_path in [
            "config/db_extract/customer_master_oracle.json",
            "config/db_extract/transaction_summary_mssql.json",
            "config/file_ingestion/orders_data_csv.json",
            "config/file_ingestion/returns_data_xlsx.json",
            "config/sharepoint/sales_forecast_sharepoint.json",
            "config/sharepoint/inventory_status_sharepoint.json"
        ]:
            router = IngestionRouter(config_path)
            router.process()
    except Exception as e:
        logger.exception("Unhandled exception in ingestion process")

if __name__ == "__main__":
    main()
