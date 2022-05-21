

from flask import Flask,render_template,request
import joblib
import numpy as np
from helpers.dummis import *

app= Flask(__name__)


model=joblib.load('models/model.h5')
scaler=joblib.load('models/scaler.h5')

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict",methods=["GET"])
def predict():
    all_data=request.args 
    
    x1_year=int(all_data["Prod_year"])
    x2_Enginevolume= float(all_data["Engine_volume"])
    x3_Mileage=int(all_data["Mileage"])
    x4_Cylinders=int(all_data["Cylinders"])
    x5_Airbags=int(all_data["Air_bags"])
    x6_Manufacturer= Manufacturer_dummies[all_data["Manufacturer"]]
    x7_Turbo= int(all_data["Turbo"])
    x8_Leatherinterior= int(all_data["Leatherinterior"])
    x9_Category= Category_dummise[all_data["Category"]]
    x10_Fueltype= Fueltype_dummies[all_data["Fueltype"]]
    x11_Gearboxtype= Gearboxtype_dummies[all_data["Gearboxtype"]]
    x12_Drivewheels= Drivewheels_dummies[all_data["Drivewheels"]]
    x13_Wheel= Wheel_dummies[all_data["Wheel"]]

    data=[x1_year,x2_Enginevolume,x3_Mileage,x4_Cylinders,x5_Airbags]+x6_Manufacturer+[x7_Turbo,x8_Leatherinterior]+x9_Category+x10_Fueltype+x11_Gearboxtype+x12_Drivewheels+x13_Wheel
    
    d=np.array(data)
    data_s= scaler.transform([d[0:5]])

    data_scaled=np.array([list(data_s[0])+list(d[5:])])

    pred= model.predict(data_scaled)[0]

    return render_template("prediction.html",price= predict_dummis[int(pred)])






if __name__=='__main__':
    app.run(debug=True, port=9000)