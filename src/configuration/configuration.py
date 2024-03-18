import os, sys
from datetime import datetime

from src.constants import *
from src.utils import *
from src.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig, DataProcessingConfig, TrainingPipelineConfig

class Configuration:
    
    def __init__(self, config_file_path:str=CONFIG_FILE_PATH) -> None:
        try:
            self.config_file_path = config_file_path
            self.config_info = read_yaml_file(self.config_file_path)
            self.time_stamp = f"{datetime.now().strftime('%Y-%m-%-%H-%M-%S')}"
            self.training_pipeline_config = self.get_training_pipeline_config()
        except Exception as e:
            raise Exception(e, sys) from e
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_config_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                self.time_stamp,
                data_ingestion_config_info[DATA_INGESTION_ARTIFACT_DIR_KEY]
            )
            dataset_file_name = data_ingestion_config_info[DATA_INGESTION_DATASET_FILE_NAME_KEY]
            dataset_file_path = os.path.join(data_ingestion_artifact_dir, dataset_file_name)
            stock_symbol = data_ingestion_config_info[DATA_INGESTION_STOCK_SYMBOL]
            data_ingestion_config = DataIngestionConfig(
                ingested_data_file_path=dataset_file_path,
                stock_symbol = stock_symbol
            )
            return data_ingestion_config
        
        except Exception as e:
            raise Exception(e, sys) from e
        
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_preprocessing_config_info = self.config_info[DATA_PREPROCESSING_CONFIG_KEY]
            data_preprocessing_artifact_dir = os.path.join(
                artifact_dir,
                self.time_stamp,
                data_preprocessing_config_info[DATA_PREPROCESSING_ARTIFACT_DIR_KEY]
            )
            preprocessing_data_file_name = data_preprocessing_config_info[DATA_PREPROCESSING_DATASET_FILE_NAME_KEY]
            preprocessing_data_file_path = os.path.join(data_preprocessing_artifact_dir, preprocessing_data_file_name)
            data_preprocessing_config = DataPreprocessingConfig(
                preprocessing_data_file_path = preprocessing_data_file_path
            )
            return data_preprocessing_config
        
        except Exception as e:
            raise Exception(e, sys) from e
        
    def get_data_processing_config(self) -> DataProcessingConfig:
        try:
            pass
        except Exception as e:
            raise Exception(e, sys) from e     
              
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR , DATA_DIR, training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            return training_pipeline_config
        except Exception as e:
            raise Exception(e, sys) from e

