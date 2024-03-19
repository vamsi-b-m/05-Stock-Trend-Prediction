import os, sys

from src.configuration.configuration import Configuration
from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import Data_Preprocessing
from src.components.data_processing import DataProcessing
from src.entity.artifact_entity import DataIngestionArtifact, DataPreprocessingArtifact, DataProcessingArtifact

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
            print(data_preprocessing_artifact)
            return data_preprocessing_artifact
        except Exception as e:
            raise Exception(e, sys) from e
        
    def start_data_processing(self, data_ingestion_artifact : DataIngestionArtifact, data_preprocessing_artifact:DataPreprocessingArtifact) -> DataProcessingArtifact:
        try:
            data_processing = DataProcessing(
                data_processing_config=self.config.get_data_processing_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_preprocessing_artifact=data_preprocessing_artifact
            )
            data_processing_artifact = data_processing.initiate_data_processing()
            return data_processing_artifact
        except Exception as e:
            raise Exception(e, sys) from e
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_preprocessing_artifact = self.start_data_preprocessing(data_ingestion_artifact=data_ingestion_artifact)
            data_processing_artifact = self.start_data_processing(data_ingestion_artifact=data_ingestion_artifact, data_preprocessing_artifact=data_preprocessing_artifact)
        except Exception as e:
            raise Exception(e, sys) from e