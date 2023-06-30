from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd

account_name = 'madhumlws981768029566'
account_key = '4vd+ucylSX+BIJs3O6/3DtDz4JOS9JlXp21yeFnNb7rX7i3vA4sQbmOI/PkaEgQMlfK+ZyvJ1+BH+AStZQJGhA=='
table_name = 'TestTextAnalytics'
table_service = TableService(account_name=account_name, account_key=account_key)

endpoint = 'https://madhutest.cognitiveservices.azure.com/'
key = 'f10906976f9540db8144b60c999e6eb9'
credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

def add_prompt_to_table(prompt_text):
    # Create an entity object
    entity = Entity()
    entity.PartitionKey = '30'
    entity.RowKey = 'Age'
    entity.PromptText = prompt_text

    # Insert the entity into the table
    table_service.insert_entity(table_name, entity)

prompt_text = 'What is the table name'
add_prompt_to_table(prompt_text)


items = table_service.query_entities('TestTextAnalytics')
for item in items:
    # Process each item retrieved from Azure Table Storage
    # You can access properties using item['property_name']
    print(item['PartitionKey'], item['RowKey'])


df = pd.DataFrame(items)
documents = df['PromptText'].tolist()
response = text_analytics_client.analyze_sentiment(documents)

# Process the sentiment analysis results
for idx, doc in enumerate(response):
    sentiment = doc.sentiment
    print(f"Sentiment for document {idx}: {sentiment}")


