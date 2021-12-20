from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('RandomForest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        crim = float(request.form['crim'])
        zn=float(request.form['zn'])
        indus=int(request.form['indus'])
        
        chas=float(request.form['chas'])
        nox=float(request.form['nox'])
        rm=float(request.form['rm'])
        age=float(request.form['age'])
        dis=float(request.form['dis'])
        rad=float(request.form['rad'])
        tax=float(request.form['tax'])
        ptratio=float(request.form['ptratio'])
        black=float(request.form['black'])
        lstat=float(request.form['lstat'])





        
        prediction=model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lstat]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this house")
        else:
            return render_template('index.html',prediction_text="the predicted price is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

