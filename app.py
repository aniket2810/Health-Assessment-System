# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import os
import numpy as np


app = Flask(__name__)               # Here we have created an flask app named 'app'


#Load the CLassifier model of diabetes disease.
filename1 = 'diabetes.pkl'
diabetes_file = pickle.load(open(filename1, 'rb'))


#Load the CLassifier model of kidney disease.
filename2 = 'kidney.pkl'
kidney_file = pickle.load(open(filename2, 'rb'))
  

#Load the CLassifier model of heart disease.
filename3 = 'heart.pkl'
heart_file = pickle.load(open(filename3, 'rb'))


# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Overview Page
@app.route('/overview')
def overview():
    return render_template('overview.html')


# Diabetes Disease Prediction
@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')


# Kidney Disease Prediction
@app.route('/kidney', methods=['GET','POST'])
def kidney():
    return render_template('kidney.html')


#Heart Disease Prediction
@app.route('/heart', methods=['GET','POST'])
def heart():
    return render_template('heart.html')


# Diabetes Prediction Page
@app.route('/diabetespredict', methods=['GET','POST'])
def diabetes_predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])

        diabetes_data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        d_prediction = diabetes_file.predict(diabetes_data)

        return render_template('diabetes_result.html', prediction=d_prediction)   


# Heart Prediction Page
@app.route('/heartpredict', methods=['GET','POST'])
def heart_predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        ca = float(request.form['ca'])
        insulin = float(request.form['insulin'])
        thal = int(request.form['thal'])

        heart_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, ca, insulin, thal]])
        h_prediction = heart_file.predict(heart_data)

        return render_template('heart_result.html', prediction=h_prediction)


# Kidney Prediction Page
@app.route('/kidneypredict', methods=['GET','POST'])
def kidney_predict():
    if request.method == 'POST':
        specific_gravity = float(request.form['specific_gravity'])
        albumin = int(request.form['albumin'])
        red_blood_cells = int(request.form['red_blood_cells'])
        pus_cell = int(request.form['pus_cell'])
        haemoglobin = float(request.form['haemoglobin'])
        hypertension = int(request.form['hypertension'])
        diabetes_mellitus = int(request.form['diabetes_mellitus'])
        appetite = int(request.form['appetite'])

        kidney_data = np.array([[specific_gravity, albumin, red_blood_cells, pus_cell, haemoglobin, hypertension,     diabetes_mellitus, appetite]])
        k_prediction = kidney_file.predict(kidney_data)

        return render_template('kidney_result.html', prediction=k_prediction)


# Kidney Prediction Page
# @app.route('/kidneypredict', methods=['GET','POST'])
# def kidney_predict():
#     if request.method == 'POST':
#         age = int(request.form['age'])
#         blood_pressure = float(request.form['blood_pressure'])
#         specific_gravity = float(request.form['specific_gravity'])
#         albumin = int(request.form['albumin'])
#         sugar = int(request.form['sugar'])
#         red_blood_cells = int(request.form['red_blood_cells'])
#         pus_cell = int(request.form['pus_cell'])
#         pus_cell_clumps = int(request.form['pus_cell_clumps'])
#         bacteria = int(request.form['bacteria'])
#         blood_glucose_random = float(request.form['blood_glucose_random'])
#         blood_urea = float(request.form['blood_urea'])
#         serum_creatinine = float(request.form['serum_creatinine'])
#         sodium = float(request.form['sodium'])
#         potassium = float(request.form['potassium'])
#         haemoglobin = float(request.form['haemoglobin'])
#         packed_cell_volume = float(request.form['packed_cell_volume'])
#         white_blood_cell_count = float(request.form['white_blood_cell_count'])
#         red_blood_cell_count = float(request.form['red_blood_cell_count'])
#         hypertension = int(request.form['hypertension'])
#         diabetes_mellitus = int(request.form['diabetes_mellitus'])
#         coronary_artery_disease = int(request.form['coronary_artery_disease'])
#         appetite = int(request.form['appetite'])
#         peda_edema = int(request.form['peda_edema'])
#         aanemia = int(request.form['aanemia'])

#         kidney_data = np.array([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]])
#         k_prediction = kidney_file.predict(kidney_data)

#         return render_template('kidney_result.html', prediction=k_prediction)
 

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

if __name__ == "__main__":
    app.run(debug=True)