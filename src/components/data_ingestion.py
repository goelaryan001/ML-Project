#Data injection basically means I will be reading a data set from a database, or it can be from some other, uh, file locations, or it can be from different kind of databases also.
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

'''
Whenever we are performing the data ingestion component, there should be some inputs that may be probably

required by this data ingestion component.

Right.

The input can be like uh, where I have to probably save the training path or train train data where

I have to probably save the test data, where I have to probably save the raw data.

Right.

So those kind of input will basically be creating in another class.

And this class I will try to mention it as data ingestion class okay.'''

'''now for decorator: Because inside a class to define the class variable you basically use it in it.
Using dataclass we can directly able to define our class variable'''
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

'''
 any input that is required

right.

Anything that I specifically require I will probably give through this particular data ingestion config.

So probably if you do data transformation also you will probably go ahead and write data transformation

config because there also you'll be requiring some kind of inputs right output with respect to any data

ingestion'''
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transormation=DataTransformation()
    data_transormation.initiate_data_transformation(train_data,test_data)