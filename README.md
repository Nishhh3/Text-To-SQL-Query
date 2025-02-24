# Text-To-SQL-Query
In this project I will be developing an end to end LLm application using Llama where we will create Text To SQL LLM App and later retrieving query from sql database

### Setup and installation
Make sure you have

- Python3 installed.
- pip installed for package management.
1. Creation of virtualenv
```sh
python3 -m venv env #Windows
pipenv install #Mac
```
2. activate virtual env
```sh
env/Scripts/activate #Windows
pipenv shell #Mac
source env/bin/activate #Linux
```
3. add the data you want in database
4. run the main.py file using streamlit server to serve the RAG
```sh
streamlit run main.py
```
