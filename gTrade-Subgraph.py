import requests
import json
from config import *

# Define the GraphQL query
query = gTRADE_QUERY

# Set the URL of the subgraph API endpoint
url = gTRADE_URL

# Send a POST request to the subgraph API with the query
response = requests.post(url, json={"query": query})
# Parse the response JSON
if response.status_code == 200:
    data= json.loads(response.text)
    print(data)
