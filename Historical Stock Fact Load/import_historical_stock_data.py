import pandas as pd
from sqlalchemy import create_engine
import time
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

password=os.getenv('password')

try:
    start_time = time.time()
    logging.info("Starting script...")

    logging.info("Loading Parquet file...")
    df = pd.read_parquet('/Users/michaelb/Project 01/Historical Stock Fact Load/historical_stock_fact.parquet')
    logging.info("Parquet file loaded successfully.")

    logging.info("Creating database engine...")
    engine = create_engine(f'postgresql://michaelb:{password}@localhost:5432/Project01')
    logging.info("Database engine created.")
    
    logging.info("Inserting data into database...")
    df.to_sql('Project01', engine, if_exists='append', index=False)
    logging.info("Data inserted into database.")

    end_time = time.time()

    duration = end_time - start_time
    logging.info(f"Operation took {duration} seconds")

except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    logging.info("Script finished.")