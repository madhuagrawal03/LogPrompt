import os
import warnings
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import pyodbc

warnings.filterwarnings('ignore')

# Replace these with your own values, either in environment variables or directly here
AZURE_OPENAI_GPT_DEPLOYMENT = os.environ.get("AZURE_OPENAI_GPT_DEPLOYMENT") or "ada"  # davinci - throttled
AZURE_OPENAI_CHATGPT_DEPLOYMENT = os.environ.get("AZURE_OPENAI_CHATGPT_DEPLOYMENT") or "chat"

os.environ["OPENAI_API_KEY"] = "" # Use your key here
# Use the current user identity to authenticate with Azure OpenAI
# just use 'az login' locally, and managed identity when deployed on Azure). If you need to use keys, u
#keys for each service.
azure_credential = DefaultAzureCredential()

dbconnection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:msdecisiondbserverdev.database.windows.net,1433;Database=msdecisiondb;Uid=msdecisiondb;Pwd=Msd$2022;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# query = "SELECT * FROM [dbo].[DownloadURIDaily]"
query = "SELECT top 500 * FROM [dbo].[DimDownlod]"
df = pd.read_sql(query, dbconnection)


agent = create_pandas_dataframe_agent(OpenAI (temperature=0), df, verbose=True)

agent.run("How many records are there?")
agent.run("Summarize by productgroup")