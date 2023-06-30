# import the required packages
import urllib
import os
import warnings
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import AzureOpenAI

warnings.filterwarnings('ignore')

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_KEY"] = "06b31ed1ea0f4db082399e37ad428063"
os.environ["OPENAI_API_BASE"] = "https://madhuopenai98.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"

llm = AzureOpenAI(deployment_name="madhudavinci", model_name="text-davinci-003") 

def db_instance():
    #Creating SQLAlchemy connection sting
    params = urllib.parse.quote_plus('Driver={ODBC Driver 18 for SQL Server};Server=tcp:msdecisiondbserverdev.database.windows.net,1433;Database=fhl;Uid=msdecisiondb;Pwd=Msd$2022;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    db_instance = SQLDatabase.from_uri(conn_str)
    return db_instance

db = db_instance()

# LangChain Agent
toolkit = SQLDatabaseToolkit(db=db, llm = llm)

agent_executor = create_sql_agent(
    llm= llm,
    toolkit=toolkit,
    verbose=True,
    top_k = 5
)

#scenario 1
agent_executor.run('use this Instructions : 1. partitionKey in CatalogLocalized data is combination of updateId and RevisionNumber with dot as delimiter. 2. partitionKey in CatalogMetadata is updateid. query : Get localized data for latest revision of update id 00039324-5cea-4ae7-90d7-be154946529a')

#scenario 2
agent_executor.run('Get the status of submission 31211c7d-3588-4f5f-aec6-451aedba938b using logs messages from data_message column. scan full table')
