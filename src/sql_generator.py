
from dotenv import load_dotenv 
from langchain_community.utilities.sql_database import SQLDatabase
import streamlit as st 
from langchain_core.messages import AIMessage , HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



class SQLGenerator : 


    def __init__(self,db) -> None:
        self.db = db 
        pass


    def get_sql_chain(self): 
        template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
        Dont provide any explanation , just give simple SQL query.
        
        <SCHEMA>{schema}</SCHEMA>
        
        Conversation History: {chat_history}
        
        
        
        For example:
        Question: which 3 artists have the most tracks?
        SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
        Question: Name 10 artists
        SQL Query: SELECT Name FROM Artist LIMIT 10;
        
        Your turn:
        
        Question: {question}
        SQL Query:
        """

        prompt = ChatPromptTemplate.from_template(template)
        #llm = ChatOpenAI()
        llm = ChatGroq()

        def get_schema(_): 
            return self.db.get_table_info()

        return (
            RunnablePassthrough.assign(schema=get_schema)
            | prompt 
            | llm
            | StrOutputParser()

        )

    def get_response(self,user_query:str , chat_history:list): 
        db = self.db
        sql_chain = self.get_sql_chain()

        template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, question, sql query, and sql response, write a natural language response.
        <SCHEMA>{schema}</SCHEMA>

        Conversation History: {chat_history}
        SQL Query: <SQL>{query}</SQL>
        User question: {question}
        SQL Response: {response}"""

        prompt = ChatPromptTemplate.from_template(template) 

        #llm = ChatOpenAI()
        llm = ChatGroq()

        chain = (
            RunnablePassthrough.assign(query=sql_chain).assign(
                schema=lambda _:db.get_table_info(),
                response = lambda vars : db.run(vars["query"]),
            )
            | prompt 
            | llm 
            | StrOutputParser()
        )

        return chain.invoke({
            "question" : user_query , 
            "chat_history" : chat_history
        })