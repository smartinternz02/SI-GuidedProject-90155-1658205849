import pandas as pd
from flask import Flask,render_template,request
app = Flask(__name__)
import pickle,joblib
model = pickle.load(open('model.pkl','rb'))
ct=joblib.load("ct")
@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesment', methods=["POST"])
def prediction():
    return render_template("index1.html")
@app.route('/model',methods=['POST'])
def admin():

    names=["Sex","Job","Checking account","Housing","Saving accounts","Purpose","Credit amount","Duration","Age",]

    sex= request.form["Sex"]
    job = request.form["Job"]
    checking_account=request.form["Checking account"]
    housing= request.form["Housing"]
    saving_account = request.form["Saving accounts"]
    purpose = request.form["Purpose"]
    credit_amount=request.form["Credit amount"]
    duration=request.form["Duration"]
    age=request.form["Age"]
    values=[[sex,job,checking_account,housing,saving_account,purpose,int(credit_amount),int(duration),int(age)]]

    data=pd.DataFrame(values,columns=names)
    data=ct.transform(data)

    a = model.predict(data)
    if (a[0]==0):
        b="Bad"
        return render_template("predbad.html",z=b)
    if (a[0]==1):
        b ="Good"
        return render_template("predgood.html",z=b)

if __name__=='__main__':
    app.run(debug =True)