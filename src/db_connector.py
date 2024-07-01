
from langchain_community.utilities.sql_database import SQLDatabase

def init_database(user:str,password:str,host:str,port:str,database:str): 
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)