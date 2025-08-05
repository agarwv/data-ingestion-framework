
import json
from src.db_ingestor import DatabaseIngestor
from src.file_ingestor import FileIngestor
from src.sharepoint_ingestor import SharePointIngestor
from src.logger import setup_logging

class IngestionRouter:
    def __init__(self, config_path):
        self.config_path = config_path
        self.logger = setup_logging()
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def process(self):
        source_type = self.config.get("source_type")
        if source_type == "db":
            ingestor = DatabaseIngestor(self.config)
        elif source_type == "file":
            ingestor = FileIngestor(self.config)
        elif source_type == "sharepoint":
            ingestor = SharePointIngestor(self.config)
        else:
            raise ValueError(f"Unsupported source_type: {source_type}")
        ingestor.ingest()
