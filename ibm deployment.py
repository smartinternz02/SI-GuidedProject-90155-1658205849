import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "IUl5hw3k8l5r0EY693dbgs2zl1yzjnyg6zJFC7WjZs3N"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [ "Sex", "Job", "Checking account", "Housing", "Saving accounts", "Purpose",
                                                 "Credit amount", "Duration","Age"],
                                       "values":[[   0.,    2.,    0.,    0.,    3.,   23.,    2., 1200.,   12.]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/91b80867-44f8-4890-9abb-7d9520fc5973/predictions?version=2022-08-09', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
pred=response_scoring.json()
print(pred)