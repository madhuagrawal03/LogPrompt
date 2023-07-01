from azure.kusto.data import KustoConnectionStringBuilder
from azure.kusto.data import KustoClient
import requests

cluster = "https://madhucluster98.eastus.kusto.windows.net"
authority = "d4e63520-bb93-45af-9800-ec723d6c5c1f"
app_id = "69ed328a-5603-4cc4-8782-5b44b6e071c2"
app_key = ""
kusto_database = "TestDB"

# Construct the connection string
connection_string = KustoConnectionStringBuilder.with_aad_application_key_authentication(
    connection_string=cluster,
    authority_id=authority,
    aad_app_id=app_id,
    app_key=app_key
)

kusto_client = KustoClient(connection_string)
subscription_key = ""
endpoint = "https://madhuopenai98.openai.azure.com/"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {subscription_key}"
}

generic_prompts = ["Show all records from TestDBTable"]
                #    "Summarize column1 by column2 from TestDBTable",
                #    "Count rows where column3 > 100 from TestDBTable"]

kusto_queries = []

for prompt in generic_prompts:
    # Prepare the request payload
    payload = {
        "inputs": {
            "prompt": prompt,
            "max_tokens": 100,
            "top_p": 1.0,
            "temperature": 0.7
        },
        "model": "text-davinci-003"
    }

    # Make the API request
    response = requests.post(endpoint, headers=headers, json=payload)
    print(response)
    response_json = response.json()

    # Extract the generated query from the response
    generated_query = response_json["choices"][0]["text"]
    kusto_queries.append(generated_query)

# Print the generated Kusto queries
for query in kusto_queries:
    print(query)


