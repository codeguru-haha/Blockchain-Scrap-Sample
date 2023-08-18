import requests
from config import *
# Define the GraphQL query
query = HMX_QUERY

# Set the URL of the subgraph API endpoint
url = HMX_URL

# Send a POST request to the subgraph API with the query
response = requests.post(url, json={"query": query})
# Parse the response JSON
data = response.json()
print(data)

