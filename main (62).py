import requests
import json

# Set up API endpoint URL
url = 'https://api.example.com/contracts'

# Set up query parameters to filter results
params = {'grant_amount': '150000', 'status': 'open'}

# Set up headers for authentication, if necessary
headers = {'Authorization': 'Bearer API_KEY'}

# Define function to query API and filter results
def check_contracts():
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        contracts = json.loads(response.text)
        for contract in contracts:
            if contract['grant_amount'] > 150000:
                # Do something with the contract data, such as send an email or log it in a database
    else:
        # Handle error response from API
        print('Error: ' + response.status_code)

# Set up a loop to run the function every 5 minutes
while True:
    check_contracts()
    time.sleep(300)
