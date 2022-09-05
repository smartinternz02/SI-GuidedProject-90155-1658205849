
import pandas as pd
from flask import Flask,render_template,request
import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "kMD7DUJcjm7ozDYxt2XipzGrx_pVecZad14qp_LdJXqt"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line


app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesment', methods=["POST","GET"])
def prediction():
    return render_template("index1.html")
@app.route('/model',methods=['POST'])
def admin():


    sex= request.form["Sex"]

    housing= request.form["Housing"]

    job = request.form["Job"]
    
    checking_account=request.form["Checking account"]

    saving_account = request.form["Saving accounts"]
    
    purpose=request.form["Purpose"]
    
    credit_amount=request.form["Credit amount"]
    
    duration=request.form["Duration"]

    age = request.form["Age"]



    d=[[int(sex),int(job) , int(checking_account) , int(housing) , int(saving_account) , int(purpose),int(credit_amount),int(duration),int(age)]]
    payload_scoring = {"input_data": [{"field": [ "Sex", "Job", "Checking account", "Housing", "Saving accounts", "Purpose",
                                                 "Credit amount", "Duration","Age"],
                                       "values":d}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/1cfe052d-078e-45ee-997a-3495864c5659/predictions?version=2022-08-09',
    json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print()
    predictions = response_scoring.json()
    print(predictions)
    predictions=predictions['predictions'][0]['values'][0][0]
    
    if (predictions==0):
        b="Bad"
        return render_template("predbad.html",z=b)
    if (predictions==1):
        b ="Good"
        return render_template("predgood.html",z=b)

if __name__=='__main__':
    app.run(debug = False)