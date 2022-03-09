import os
import re
from flask import Flask, render_template, request
app = Flask(__name__)
import numpy as np
import joblib

loaded_model_stress = joblib.load('Random_Forest_Stress.pkl')
loaded_model_anxiety = joblib.load('Random_Forest_Anxiety.pkl')
loaded_model_depression = joblib.load('Random_Forest_Depression.pkl')
def Prediction_value_stress(to_predict_list):
    to_predict = np.array(to_predict_list)
    result_stress = loaded_model_stress.predict(to_predict)
    return result_stress[0]
def Prediction_value_anxiety(to_predict_list):
    to_predict = np.array(to_predict_list)
    result_anxiety = loaded_model_anxiety.predict(to_predict)
    return result_anxiety[0]
def Prediction_value_depression(to_predict_list):
    to_predict = np.array(to_predict_list)
    result_depression = loaded_model_depression.predict(to_predict)
    return result_depression[0]
 
@app.route('/', methods = ['GET'])
def index():
    return render_template("ddd.html")

@app.route('/result', methods = ['POST'])
def result():
    to_predict_list = request.json
    print(to_predict_list)
    to_predict_list = list(to_predict_list.values())
    # print(str(to_predict_list))
    to_predict_list = list(map(int, to_predict_list))
    result_stress = Prediction_value_stress([to_predict_list])  
    result_anxiety = Prediction_value_anxiety([to_predict_list]) 
    result_depression = Prediction_value_depression([to_predict_list]) 
    if int(result_stress)== 0:
        prediction_stress ='Minimal Stress'
    elif int(result_stress)== 1:
        prediction_stress ='Mild Stress' 
    elif int(result_stress)== 2:
        prediction_stress ='Moderately Severe Stress' 
    else:          
        prediction_stress ='Severe Stress'
    
    if int(result_anxiety)== 0:
        prediction_anxiety ='Minimal Anxiety'
    elif int(result_anxiety)== 1:
        prediction_anxiety ='Mild Anxiety' 
    elif int(result_anxiety)== 2:
        prediction_anxiety ='Moderately Severe Anxiety' 
    else:          
        prediction_anxiety ='Severe Anxiety'

    if int(result_depression)== 0:
        prediction_depression ='None'
    elif int(result_depression)== 1:
        prediction_depression ='Mild Depression' 
    elif int(result_depression)== 2:
        prediction_depression ='Moderate Depression'
    elif int(result_depression)== 3:
        prediction_depression ='Moderately Severe Depression' 
    else:          
        prediction_depression ='Severe Depression'
    # a = {}
    return { "Stress Level": prediction_stress , "Anxiety Level":prediction_anxiety ,"Depression Level":prediction_depression}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True, port=port)

