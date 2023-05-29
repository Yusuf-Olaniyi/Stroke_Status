# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:34:29 2022

@author: YUSUF
"""

import streamlit as st
import pickle
import pandas as pd


stroke_status_predictor = open('stroke_status_predictor.pkl','rb')
classifier = pickle.load(stroke_status_predictor)

def stroke_predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
    df = pd.DataFrame({'gender':gender, 'age':age, 'hypertension':hypertension, 'heart_disease':
                       heart_disease, 'ever_married':ever_married,'work_type':work_type, 
                       'Residence_type':Residence_type, 'avg_glucose_level':avg_glucose_level, 
                       'bmi':bmi,'smoking_status':smoking_status},index=pd.Series(1))
    return classifier.predict(df)

   
def main():
    st.title('Stroke Status Predictor')
   
    
    gender = st.radio('Gender',['Male','Female','Other'])
    if gender == 'Male':
        gender = 1
    elif gender == 'Female':
        gender = 0
    else:
        gender = 2
    
    age = st.number_input('Age',min_value=0,max_value=100)
    
    hypertension = st.radio('Hypertensive',['Yes','No'])
    if hypertension == 'Yes':
        hypertension = 1
    else:
        hypertension = 0
    
    heart_disease = st.radio('Do you have any Heart Disease?',['Yes','No'])
    if heart_disease == 'Yes':
        heart_disease = 1
    else:
        heart_disease = 0
        
    ever_married = st.radio('Ever Married',['Yes','No'])
    if ever_married == 'Yes':
        ever_married = 1
    else:
        ever_married = 0
    
    work_type = st.radio('Work Nature',['Private','Self Employed','Children','Government Job','Never Worked'])
    if work_type == 'Private':
        work_type = 2
    elif work_type == 'Self Employed':
        work_type = 3
    elif work_type == 'Children':
        work_type = 4
    elif work_type == 'Government Job':
        work_type = 0
    else:
        work_type = 1
        
    Residence_type = st.radio('Residence Type',['Urban','Rural'])
    if Residence_type == 'Urban':
        Residence_type = 1
    else:
        Residence_type = 0
    
    bmi = st.slider('Body Mass Index',0,39,25)
    
    avg_glucose_level = st.slider('Average Glucose Level',20,280,100)
    
    smoking_status = st.radio('Smoking Status',['Smokes','Formerly smokes','Never smoked','Unknown'])
    if smoking_status == 'Smokes':
        smoking_status = 3
    elif smoking_status == 'Formerly smokes':
        smoking_status = 1
    elif smoking_status == 'Never smoked':
        smoking_status = 2
    else:
        smoking_status = 0
    
    result = ''
    if st.button('Predict'):
        result = stroke_predict(gender,age,hypertension,heart_disease,
                       ever_married,work_type,Residence_type,
                       avg_glucose_level,bmi,smoking_status)

    if result == 1:    
        st.success('You are likely to have stroke')
    else:
        st.success('You are not likely to have stroke')
        

if __name__=='__main__':
    main()