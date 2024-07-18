import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig
from train_model import ModelTrainerConfig
from train_model import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('df2',"train.csv")
    test_data_path: str=os.path.join('df2',"test.csv")
    raw_data_path: str=os.path.join('df2',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(os.path.join('dataset','dataset.csv'))
    
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)


            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise e
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    best_model = modeltrainer.initiate_model_trainer(train_arr,test_arr)