import os, sys

from src.configuration.configuration import Configuration
from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import Data_Preprocessing
from src.entity.artifact_entity import DataIngestionArtifact, DataPreprocessingArtifact

class Pipeline:

    def __init__(self, config : Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise Exception(e, sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=self.config.get_data_ingestion_config()
                )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise Exception(e, sys) from e
    
    def start_data_preprocessing(self, data_ingestion_artifact : DataIngestionArtifact) -> DataPreprocessingArtifact:
        try:
            data_preprocessing = Data_Preprocessing(
                data_preprocessing_config=self.config.get_data_preprocessing_config(),
                data_ingestion_artifact=data_ingestion_artifact
            )
            data_preprocessing_artifact = data_preprocessing.initiate_data_preprocessing()
            return data_preprocessing_artifact
        except Exception as e:
            raise Exception(e, sys) from e
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_preprocessing_artifact = self.start_data_preprocessing(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise Exception(e, sys) from e