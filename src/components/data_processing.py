import os, sys
import logging

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from src.utils import *
from src.entity.config_entity import DataProcessingConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataPreprocessingArtifact, DataProcessingArtifact


class DataProcessing:

    def __init__(self, data_processing_config:DataProcessingConfig, data_ingestion_artifact:DataIngestionArtifact, data_preprocessing_artifact:DataPreprocessingArtifact) -> None:
        try:
            self.data_processing_config = data_processing_config
            self.data_preprocessing_artifact = data_preprocessing_artifact
            self.data_ingestion_artifact = data_ingestion_artifact
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

        except Exception as e:
            raise Exception(e, sys) from e
        
    def get_moving_averages(self):
        try:
            self.ma50 = self.dataset['Close'].rolling(50).mean()
            self.ma100 = self.dataset['Close'].rolling(100).mean()
            self.ma200 = self.dataset['Close'].rolling(200).mean()

            processing_moving_averages_dir_path = self.data_processing_config.processing_moving_averages_dir_path
            os.makedirs(processing_moving_averages_dir_path, exist_ok=True)

            processing_fifty_moving_average_file_path = self.data_processing_config.processing_fifty_moving_average_file_path
            write_csv_file(self.ma50, processing_fifty_moving_average_file_path)

            processing_hundred_moving_average_file_path = self.data_processing_config.processing_hundred_moving_average_file_path
            write_csv_file(self.ma100, processing_hundred_moving_average_file_path)

            processing_two_hundred_moving_average_file_path = self.data_processing_config.processing_two_hundred_moving_average_file_path
            write_csv_file(self.ma200, processing_two_hundred_moving_average_file_path)
            
        except Exception as e:
            raise Exception(e, sys) from e
        
    def generate_graphs(self):
        try:
            stock_name = self.data_ingestion_artifact.stock_symbol[:-3]
            processing_graphs_file_path = self.data_processing_config.processing_graphs_file_path
            self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])

            # Plotting the Close Price and Moving Averages
            fig, axs = plt.subplots(5, 1, figsize=(10, 30))

            # Close Price
            axs[0].set_title(f'{stock_name}\n\nStock Close Price Over Time')
            axs[0].plot(self.dataset['Date'], self.dataset['Close'])
            axs[0].set_xlabel('Date')
            axs[0].set_ylabel('Close Price')
            
            # 50 Moving Average
            axs[1].set_title("\n50 Moving Average")
            axs[1].plot(self.dataset['Date'], self.dataset['Close'])  
            axs[1].plot(self.dataset['Date'], self.ma50)
            axs[1].set_xlabel('Date')

            # 100 Moving Average
            axs[2].set_title("\n100 Moving Average")
            axs[2].plot(self.dataset['Date'], self.dataset['Close'])  
            axs[2].plot(self.dataset['Date'], self.ma100)
            axs[2].set_xlabel('Date')

            # 200 Moving Average
            axs[3].set_title("\n200 Moving Average")
            axs[3].plot(self.dataset['Date'], self.dataset['Close'])  
            axs[3].plot(self.dataset['Date'], self.ma200)
            axs[3].set_xlabel('Date')

            # Comparing all the Moving Averages
            axs[4].set_title("\nComparing all the Moving Averages")
            axs[4].plot(self.dataset['Date'], self.dataset['Close'])  
            axs[4].plot(self.dataset['Date'], self.ma50, 'r', label='50 Moving Average')
            axs[4].plot(self.dataset['Date'], self.ma100, 'b', label='100 Moving Average')
            axs[4].plot(self.dataset['Date'], self.ma200, 'g', label='200 Moving Average')
            axs[4].set_xlabel('Date')
            axs[4].legend()

            # Set the locator to display only years on the x-axis
            plt.gca().xaxis.set_major_locator(mdates.YearLocator())
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

            # Adjust space between subplots
            plt.subplots_adjust(hspace=1)
            plt.tight_layout()
            plt.savefig(processing_graphs_file_path)

        except Exception as e:
            print("Error:", e)

    def get_processed_data(self):
        try:
            preprocessed_data_file_path = self.data_preprocessing_artifact.preprocessed_data_file_path
            self.dataset = read_csv_file(preprocessed_data_file_path)
            
            processed_data_file_path  = self.data_processing_config.processing_data_file_path
            processed_data_file_dir = os.path.dirname(processed_data_file_path)
            os.makedirs(processed_data_file_dir)

            self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])
            self.dataset = self.dataset[['Date', 'Close']]
            self.dataset = self.dataset.reset_index()
            self.dataset.to_csv(processed_data_file_path, index=False, date_format='%Y-%m-%d')
            self.dataset = read_csv_file(processed_data_file_path)

            self.get_moving_averages()
            processed_graphs_file_path = self.generate_graphs()

            is_processed = True
            message = "Data Processing Completed"

            data_processing_artifact = DataProcessingArtifact(
                processed_data_file_path = processed_data_file_path,
                processed_graphs_file_path = processed_graphs_file_path,
                is_processed=is_processed,
                message=message
            )

            return data_processing_artifact
        
        except Exception as e:
            raise Exception(e, sys) from e
        
    def initiate_data_processing(self) -> DataProcessingArtifact:
        try:
            data_processing_artifact = self.get_processed_data()
            return data_processing_artifact
        except Exception as e:
            raise Exception(e, sys) from e