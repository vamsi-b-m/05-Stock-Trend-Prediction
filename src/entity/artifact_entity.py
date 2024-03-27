from collections import namedtuple

DataIngestionArtifact = namedtuple('DataIngestionArtifact', ["ingested_data_file_path", "stock_symbol", "is_ingested", "message"])
DataPreprocessingArtifact = namedtuple('DataPreprocessingArtifact', ["preprocessed_data_file_path", "is_preprocessed", "message"])
DataProcessingArtifact = namedtuple("DataProcessingArtifact", ["processed_data_file_path", "processed_graphs_file_path", "is_processed", "message"])

ModelTrainingArtifact = namedtuple("ModelTrainingArtifact", ["train_data_file_path", "test_data_file_path", "model_file_path"])