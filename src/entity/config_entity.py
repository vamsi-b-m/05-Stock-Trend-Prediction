from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", ["ingested_data_file_path", "stock_symbol"])
DataPreprocessingConfig = namedtuple("DataPreprocessingConfig", ["preprocessing_data_file_path"])
DataProcessingConfig = namedtuple("DataProcessingConfig", ["processing_data_file_path", "processing_moving_averages_dir_path", "processing_fifty_moving_average_file_path", "processing_hundred_moving_average_file_path", "processing_two_hundred_moving_average_file_path", "processing_graphs_file_path"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig", ["model_data_dir", "model_train_data_file_path", "model_test_data_file_path", "model_file_path"])



TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir", "model_data_dir"])