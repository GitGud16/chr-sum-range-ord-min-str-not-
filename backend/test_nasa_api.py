import requests
from requests.auth import HTTPBasicAuth

# Define your EarthData username and password
username = "abdulqadirsgf"
password = "Pa@75139713971"

# Set up the authentication using HTTP Basic Auth
auth = HTTPBasicAuth(username, password)

# Example API endpoint for getting information
url = "https://urs.earthdata.nasa.gov/api/users"

# Make a request to the EarthData API
response = requests.get(url, auth=auth)

# Check if the request was successful
if response.status_code == 200:
    print("Request Successful")
    print("Response:", response.json())  # Print JSON response
else:
    print(f"Request Failed: {response.status_code}")

# Define API token
api_token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImFiZHVscWFkaXJzZ2YiLCJleHAiOjE3MzMyMzcwNzgsImlhdCI6MTcyODA1MzA3OCwiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292In0.Hk-ConiQ2F-_s2IEwmryvqBnkjsH7srGdCxcv5XNxo71hhke5FNiN_6xpvihKaVQL7Iz4z8zSBVP_8_PlaGuiNfKx9Hl6xMEZU2pZkPeRdqqWkG98V_8yJTRzxavEifcCRQKt_IFtosR01rpyrysiQ9LTtkp1luHnWIZrqjJ2TQPO0VZFfhmtz6BluhVaOtYd6x8dOTvZERFlNXBKjtdYo_HG9PkSy_TGIiSRnw2y2N9BCt1BaCNrugU_VqgTT-7F32fdm6LKYhFiyVFp-aCywrUQwXYm-8A1yYddGh6bg8UTaDjtazt7b0f5RjtJRWR4dlZnqGC74RLJkLeFQKayA'
# Define headers for the request
headers = {"Authorization": f"Bearer {api_token}"}

# Make a request with the token
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request Successful")
else:
    print(f"Request Failed: {response.status_code}")
