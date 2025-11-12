# ETL Script to push data to Mongodb database

import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# certifi library consists of Mozilla's carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            logging.info("Loaded data from CSV")

            data.reset_index(drop=True,inplace=True)

            records=list(json.loads(data.T.to_json()).values()) # .T - Transpose
            logging.info(f"Records converted successfully from csv to json format")
            return records
        except Exception as e:
            logging.error("Error occurred while converting csv to json")
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            logging.info("Connected to Mongodb database successfully")

            self.collection.insert_many(self.records)

            logging.info(f"Records inserted successfully into Mongodb database: {database} and collection: {collection}")
            return(len(self.records))
        except Exception as e:
            logging.error("Error occurred while inserting data into Mongodb")
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH=r"data_local\phisingData.csv"
    DATABASE="PhishingDataDB"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    #print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        


