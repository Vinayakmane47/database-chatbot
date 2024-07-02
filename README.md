# Text-to-SQL Chatbot

This project is a Text-to-SQL chatbot built using LangChain and Retrieval-Augmented Generation (RAG). The chatbot enables users to input natural language queries, which are then converted into SQL queries to retrieve information from a database.

### Features

- Natural Language Understanding: Convert user queries in natural language to SQL queries.
- Retrieval-Augmented Generation (RAG): Enhance the chatbot's capability to generate accurate SQL queries using retrieval-based methods.
- LangChain Integration: Utilize LangChain for natural language processing and query generation.
- Database Interaction: Execute the generated SQL queries on a connected database to fetch the required information.


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




