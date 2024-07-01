import streamlit as st
from langchain_community.utilities.sql_database import SQLDatabase
from src.sql_generator import invoke_chain
from langchain_core.messages import AIMessage, HumanMessage

st.title("Database Chatbot")

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

# Initialize session state for chat history and database
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage("Hello! I'm a database assistant. Ask me anything about your database."),
        HumanMessage("hi")
    ]

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application for databases. Connect to your preferred database type:")

    # Database type switcher
    db_type = st.selectbox("Select Database Type", ["MySQL", "PostgreSQL", "MongoDB"])

    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306" if db_type == "MySQL" else "5432" if db_type == "PostgreSQL" else "27017", key="Port")
    st.text_input("User", value="root" if db_type == "MySQL" or db_type == "PostgreSQL" else "admin", key="User")
    st.text_input("Password", type="password", value="sak$103138" if db_type == "MySQL" else "your_password", key="Password")
    st.text_input("Database", value="classicmodels" if db_type == "MySQL" or db_type == "PostgreSQL" else "mydatabase", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to Database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state['Password'],
                st.session_state['Host'],
                st.session_state['Port'],
                st.session_state['Database'],
                db_type
            )
            st.session_state.db = db
            st.success("Connected to database!")

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            response = invoke_chain(st.session_state.db, prompt, st.session_state.messages)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
