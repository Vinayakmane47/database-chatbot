# Database Chatbot

This project is a Text-to-SQL chatbot built using LangChain and Retrieval-Augmented Generation (RAG). The chatbot enables users to input natural language queries, which are then converted into SQL queries to retrieve information from a database.


### Demo : 
#### Video Link 

## Watch the Video

[![Watch the video](https://youtu.be/sax2rbURoY4)





### Features

- The chatbot converts user queries in natural language to SQL queries, enabling seamless interaction without requiring the user to know SQL
- It enhances the chatbot's capability to generate accurate SQL queries using retrieval-based methods, ensuring the most relevant information is used
- The chatbot utilizes LangChain for natural language processing and query generation, leveraging the power of OpenAI to improve query accuracy and relevancy.
- The chatbot connects to any database, executes the generated SQL queries, and fetches the required information. It only interacts with those tables which are relevant, ensuring efficient and targeted data retrieval.


### Installation 

1. Clone the repository :
   
   `git clone https://github.com/Vinayakmane47/mysql-chatbot-openai`

2. Create virtual environment :

   `conda create -p venv python==3.10 -y`
   
   `conda activate venv`

4. Install required packages :

   `pip install -r requirements.txt` 

5. Run the main.y file

   `streamlit run main.py`


### Project Structure : 
```bash
database-chatbot-openai/
│
├── data/
│   ├── sample_data.sql       # Sample data to populate the database
│
├── src/
│   ├── __init__.py
│   ├── prompts.py            # Prompts used for the project
│   ├── sql_generator.py      # Module for generating SQL queries
│   ├── db_connector.py       # Module for database connection and interaction
│   ├── config.py             # Configuration file for database settings
│   ├── examples.py           # Few-shot prompt examples 
│   ├── table_chains.py       # Chains related to which table to use for project
│
├── tests/
│   ├── test_chatbot.py       # Unit tests for the chatbot
│
├── .gitignore
├── README.md
├── requirements.txt          # List of project dependencies
└── main.py                   # Entry point for running the chatbot

```


### Configuration
#### Database Configuration: 
Update the config.py file with the necessary database connection details such as host, port, username, password, and database name.

``` bash
# config.py

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database'
```




