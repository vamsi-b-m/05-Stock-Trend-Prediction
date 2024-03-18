import os, sys
import logging

import pandas as pd

from src.utils import *
from src.entity.config_entity import DataPreprocessingConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataPreprocessingArtifact

class Data_Preprocessing:

    def __init__(self, data_preprocessing_config:DataPreprocessingConfig, data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            self.data_preprocessing_config = data_preprocessing_config
            self.data_ingestion_artifact = data_ingestion_artifact
            ingested_data_file_path = self.data_ingestion_artifact.ingested_data_file_path
            print(ingested_data_file_path)
            self.dataset = read_csv_file(ingested_data_file_path)
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e
        
    def feature_selection(self):
        try:
            self.logger.info("Started Feature Selection")
            self.dataset.head()
            self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])
            self.dataset = self.dataset[['Date', 'Close']]
            self.logger.info(f"Selected the Features {self.dataset.columns}\n")
            self.logger.info("Completed Feature Selection")
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e
        
    def handle_null_values(self):
        try:
            self.logger.info("Started Handling Null Values")
            if self.dataset.isna().any().any():
                self.dataset = self.dataset.dropna()
            else:
                pass
            self.logger.info("Completed Handling Null Values")
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e
    
    def handle_duplicate_values(self):
        try:
            self.logger.info("Started Handling Duplicates")
            if self.dataset.duplicated().any():  # Check if any duplicate rows exist
                self.dataset = self.dataset.drop_duplicates()
            else:
                pass
            self.logger.info("Completed Handling Duplicates")
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e
        
    def get_preprocessed_data(self):
        try:
            self.feature_selection()
            self.handle_null_values()
            self.handle_duplicate_values()
            preprocessed_data_file_path = self.data_preprocessing_config.preprocessing_data_file_path
            preprocessed_data_dir_path = os.path.dirname(preprocessed_data_file_path)
            os.makedirs(preprocessed_data_dir_path, exist_ok=True)
            self.dataset.to_csv(preprocessed_data_file_path, index=False)
            is_preprocessed = True
            message = "Data Preprocessing is Completed"
            data_preprocessing_artifact = DataPreprocessingArtifact(
                preprocessed_data_file_path=preprocessed_data_file_path,
                is_preprocessed=is_preprocessed,
                message=message
            )
            return data_preprocessing_artifact
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e
        
    def initiate_data_preprocessing(self):
        try:
            self.logger.info("Started Data Preprocessing")
            self.get_preprocessed_data()
            self.logger.info("Completeds Data Preprocessing")
        except Exception as e:
            self.logger.error(e)
            raise Exception(e, sys) from e







# data_dir = "data"
# data_preprocessing_artifact_dir_name = "data_preprocessing"
# data_preprocessing_artifact_dir_path = os.path.join(data_dir, data_preprocessing_artifact_dir_name)
# os.makedirs(data_preprocessing_artifact_dir_path, exist_ok=True)

# data_preprocessed_filename = "preprocessed_dataset.csv"
# data_preprocessed_filepath = os.path.join(data_preprocessing_artifact_dir_path, data_preprocessed_filename)

# try:
#     dataset = pd.read_csv("/Users/vambat1/Documents/Projects/Machine-Learning/05-Stock-Trend-Prediction/data/data_ingestion/TATASTEEL.csv")

#     dataset['Date'] = pd.to_datetime(dataset['Date'])

#     dataset = dataset[['Date', 'Close']]

#     # Handling Null Values
#     if dataset.isna().any().any():  # Check if any value is null
#         dataset = dataset.dropna()
#     else:
#         pass



#     dataset.to_csv(data_preprocessed_filepath, index=False)
# except Exception as e:
#     print(f"Exception : {e}")
