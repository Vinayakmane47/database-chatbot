from dotenv import load_dotenv 
from langchain_community.utilities.sql_database import SQLDatabase
import streamlit as st 


load_dotenv()

def init_database(user:str,password:str,host:str,port:str,database:str): 
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


st.set_page_config(page_title="Chat with MySQL",page_icon="speech_balloon")

st.title("Chat with MySQL")


with st.sidebar: 
    st.subheader("Settings") 
    st.write("This is simple chay application using MySQL . Connect to database ")

    st.text_input("Host",value="localhost",key="Host")
    st.text_input("Port",value="3306",key="Port")
    st.text_input("User",value="root",key="User")
    st.text_input("Password",type="password", value="admin",key="Password")
    st.text_input("Database",value="classicmodels",key="Database")

    if st.button("Connect"): 
        with st.spinner("Connecting to Database...."): 
            db = init_database(
            st.session_state["User"],
            st.session_state['Password'] ,
            st.session_state['Host'],
            st.session_state['Port'],
            st.session_state['Database']
            ) 
            st.session_state.db = db 
            st.success("Connected to database!")




st.chat_input("Enter your message.....")


