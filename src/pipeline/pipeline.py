import os, sys

from src.configuration.configuration import Configuration
from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import Data_Preprocessing
from src.components.data_processing import DataProcessing
from src.components.model_training import ModelTraining
from src.components.model_prediction import ModelPrediction
from src.entity.artifact_entity import DataIngestionArtifact, DataPreprocessingArtifact, DataProcessingArtifact, ModelTrainingArtifact, ModelPredictionArtifact

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
        
    def start_model_training(self, data_processing_artifact:DataPreprocessingArtifact) -> ModelTrainingArtifact:
        try:
            model_training = ModelTraining(
                model_training_config=self.config.get_model_training_config(),
                data_processing_artifact=data_processing_artifact
            )
            model_training_artifact = model_training.initiate_model_training()
            return model_training_artifact
        except Exception as e:
            raise Exception(e, sys) from e
    
    def start_model_prediction(self, model_training_artifact: ModelTrainingArtifact) -> ModelPredictionArtifact:
        try:
            model_prediction = ModelPrediction(
                model_prediction_config=self.config.get_model_prediction_config(),
                model_training_artifact=model_training_artifact
            )
            model_prediction_artifact = model_prediction.initiate_model_prediction()
            return model_prediction_artifact
        except Exception as e:
            raise Exception(e, sys) from e
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_preprocessing_artifact = self.start_data_preprocessing(data_ingestion_artifact=data_ingestion_artifact)
            data_processing_artifact = self.start_data_processing(data_ingestion_artifact=data_ingestion_artifact, data_preprocessing_artifact=data_preprocessing_artifact)
            model_training_artifact = self.start_model_training(data_processing_artifact=data_processing_artifact)
            model_prediction_artifact = self.start_model_prediction(model_training_artifact=model_training_artifact)
        except Exception as e:
            raise Exception(e, sys) from e