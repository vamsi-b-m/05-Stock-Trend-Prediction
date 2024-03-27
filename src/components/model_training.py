import os, sys

import pandas as pd
import numpy as np

from src.utils import *
from src.entity.config_entity import ModelTrainingConfig
from src.entity.artifact_entity import DataProcessingArtifact, ModelTrainingArtifact


class ModelTraining:

    def __init__(self, model_training_config:ModelTrainingConfig, data_processing_artifact:DataProcessingArtifact) -> None:
        try:
            self.model_training_config = model_training_config
            self.data_processing_artifact = data_processing_artifact
        except Exception as e:
            raise Exception(e, sys) from e
    
    def train_test_split(self):
        try:
            # Dividing the dataset into Train and Test
            self.train_dataset = pd.DataFrame(self.dataset['Close'][0:int(len(self.dataset)*0.70)])
            self.test_dataset = pd.DataFrame(self.dataset['Close'][int(len(self.dataset)*0.70):int(len(self.dataset))])

            model_data_dir = self.model_training_config.model_data_dir
            os.makedirs(model_data_dir, exist_ok=True)

            train_data_file_path = self.model_training_config.model_train_data_file_path
            test_data_file_path = self.model_training_config.model_test_data_file_path

            write_csv_file(dataset=self.train_dataset, file_path=train_data_file_path)
            write_csv_file(dataset=self.test_dataset, file_path=test_data_file_path)

            return train_data_file_path, test_data_file_path
        
        except Exception as e:
            raise Exception(e, sys) from e 

    def feature_scaling(self):
        try:
            from sklearn.preprocessing import MinMaxScaler

            scaler = MinMaxScaler(feature_range=(0,1))

            self.data_train_arr = scaler.fit_transform(self.train_dataset)

            self.x_train = []
            self.y_train = []

            for i in range(100, self.data_train_arr.shape[0]):
                self.x_train.append(self.data_train_arr[i-100:i])
                self.y_train.append(self.data_train_arr[i, 0])

            self.x_train, self.y_train = np.array(self.x_train), np.array(self.y_train)

        except Exception as e:
            raise Exception(e, sys) from e

    def train_model(self):
        try:

            model_file_path = self.model_training_config.model_file_path

            if not os.path.exists(model_file_path):
                from keras.layers import Dense, Dropout, LSTM
                from keras.models import Sequential

                model = Sequential()

                # Layer 1
                model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(self.x_train.shape[1],1)))
                model.add(Dropout(0.2))

                # Layer 2
                model.add(LSTM(units=60, activation='relu', return_sequences=True))
                model.add(Dropout(0.3))

                # Layer 3
                model.add(LSTM(units=80, activation='relu', return_sequences=True))
                model.add(Dropout(0.4))

                # Layer 4
                model.add(LSTM(units=120, activation='relu'))
                model.add(Dropout(0.5))

                # Layer 5
                model.add(Dense(units=1))

                # Summary Generation
                model_summary = model.summary()

                print(model_summary)

                model.compile(optimizer="adam", loss='mean_squared_error')
                model.fit(self.x_train, self.y_train, epochs=50)

                model.save(model_file_path)

                return model_file_path
            else:
                pass

        except Exception as e:
            raise Exception(e, sys) from e
        
    def get_model_training_config(self):
        try:
            processed_data_file_path = self.data_processing_artifact.processed_data_file_path
            self.dataset = read_csv_file(file_path=processed_data_file_path)
            train_data_file_path, test_data_file_path = self.train_test_split()
            self.feature_scaling()
            model_file_path = self.train_model()

            model_training_artifact = ModelTrainingArtifact(
                train_data_file_path = train_data_file_path,
                test_data_file_path = test_data_file_path,
                model_file_path = model_file_path
            )
            return model_training_artifact
        except Exception as e:
            raise Exception(e, sys) from e
        
    def initiate_model_training(self) -> ModelTrainingArtifact:
        try:
            model_training_artifact = self.get_model_training_config()
            return model_training_artifact
        except Exception as e:
            raise Exception(e, sys) from e