# Load your env variables
from dotenv import load_dotenv
load_dotenv()

# Import your dependencies
import os
import sys
from nylas import APIClient

# Initialize your Nylas API client
nylas = APIClient(
    os.environ.get('CLIENT_ID'),
    os.environ.get('CLIENT_SECRET'),
    os.environ.get('ACCESS_TOKEN')
)

# Return token information
token = nylas.token_info()

#Print token information
print(token)
