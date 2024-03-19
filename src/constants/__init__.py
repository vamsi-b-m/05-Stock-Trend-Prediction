import os, sys

ROOT_DIR = os.getcwd()
DATA_DIR = "data"
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
MODEL_DIR = "model"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

# Training pipeline related varibales
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data Ingestion Related Constants
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR_KEY = "data_ingestion_dir"
DATA_INGESTION_DATASET_FILE_NAME_KEY = "ingestion_dataset_file_name"
DATA_INGESTION_STOCK_SYMBOL = "stock_symbol"

# Data Preprocessing Related Constants
DATA_PREPROCESSING_CONFIG_KEY = "data_preprocessing_config"
DATA_PREPROCESSING_ARTIFACT_DIR_KEY = "data_preprocessing_dir"
DATA_PREPROCESSING_DATASET_FILE_NAME_KEY = "preprocessing_dataset_file_name"

# Data Processing Related Constants
DATA_PROCESSING_CONFIG_KEY = "data_processing_config"
DATA_PROCESSING_ARTIFACT_DIR_KEY = "data_processing_dir"
DATA_PROCESSING_DATASET_FILE_NAME_KEY = "processing_dataset_file_name"
DATA_PROCESSING_MOVING_AVERAGES_DIR_KEY = "processing_data_moving_averages_dir"
DATA_PROCESSING_FIFTY_MOVING_AVERAGE_FILE_NAME_KEY = "fifty_moving_avg_file"
DATA_PROCESSING_HUNDRED_MOVING_AVERAGE_FILE_NAME_KEY = "hundred_moving_avg_file"
DATA_PROCESSING_TWO_HUNDRED_MOVING_AVERAGE_FILE_NAME_KEY = "two_hundred_moving_avg_file"
DATA_PROCESSING_GRAPHS_FILE_NAME_KEY = "graphs_file_name"