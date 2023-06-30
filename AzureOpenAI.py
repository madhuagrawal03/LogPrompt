import os
import warnings

import pandas as pd
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import AzureOpenAI

warnings.filterwarnings('ignore')

dbconnection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:msdecisiondbserverdev.database.windows.net,1433;Database=msdecisiondb;Uid=msdecisiondb;Pwd=Msd$2022;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# query = "SELECT * FROM [dbo].[DownloadURIDaily]"
query = "SELECT top 100 * FROM [dbo].[DimDownlod]"
df = pd.read_sql(query, dbconnection)
# print(df.head(10))


os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_KEY"] = "06b31ed1ea0f4db082399e37ad428063"
os.environ["OPENAI_API_BASE"] = "https://madhuopenai98.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"

llm = AzureOpenAI(deployment_name="madhudavinci", model_name="text-davinci-003") 

agent = create_pandas_dataframe_agent(llm, df, verbose=True)
agent.run("How many records are there?")
agent.run("Summarize by productgroup")
