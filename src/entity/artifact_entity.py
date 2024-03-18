from collections import namedtuple

DataIngestionArtifact = namedtuple('DataIngestionArtifact', ["ingested_data_file_path", "is_ingested", "message"])
DataPreprocessingArtifact = namedtuple('DataPreprocessingArtifact', ["preprocessed_data_file_path", "is_preprocessed", "message"])