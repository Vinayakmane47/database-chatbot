
from langchain_community.utilities.sql_database import SQLDatabase
import streamlit as st 



# Function to initialize different database connections
def init_database(user, password, host, port, database, db_type):
    if db_type == "MySQL":
        db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        return SQLDatabase.from_uri(db_uri)
    elif db_type == "PostgreSQL":
        db_uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        return SQLDatabase.from_uri(db_uri)  # Assuming you have PostgreSQL setup similar to MySQL
    elif db_type == "MongoDB":
        from pymongo import MongoClient
        client = MongoClient(host, int(port))
        db = client[database]
        return db  # Return MongoDB client object
    else:
        raise ValueError("Unsupported database type")