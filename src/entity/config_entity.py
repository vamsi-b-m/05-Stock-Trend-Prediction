from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", ["ingested_data_file_path", "stock_symbol"])
DataPreprocessingConfig = namedtuple("DataPreprocessingConfig", ["preprocessing_data_file_path"])
DataProcessingConfig = namedtuple("DataProcessingConfig", ["processed_data_file_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])