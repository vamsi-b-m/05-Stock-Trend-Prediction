from collections import namedtuple

DataIngestionArtifact = namedtuple('DataIngestionArtifact', ["ingested_data_file_path", "is_ingested", "message"])