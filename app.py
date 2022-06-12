# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:06:25 2020

@author: kumar
"""


import numpy as np
from joblib import load
import matplotlib.image as mpimg  
import streamlit as st

rr = load('model.joblib')
st.write("""
# URBAN WATER QUALITY PREDICTION
""")
log = mpimg.imread('ipl.jpg')
st.sidebar.image(log,use_column_width=True)
activites = ["Welcome","Water Test"]
choice = st.sidebar.selectbox("Select Actvity", activites)
if choice == 'Welcome':
    st.write("A **big heartfelt Thanks** for your time in trying our Water Quality Prediction tool.")
    st.write("Urban water quality prediction project is a web-based application that uses Machine learning algorithms. That is, this application can be accessed from anywhere once the internet connection is provided. This application is intended to measure the water quality of the water in the areas like cities or urban areas, where the water pollution is high. It gives the result whether the tested water sample is polluted or not precisely and accurately. It has an interface so that user can give the input and can get very accurate results on the go. This project is developed so as to know the quality of water in polluted areas such as cities and urban areas. ")
    st.write("""If we know the water quality, we can prevent the pollutants from being mixed with the freshwater resources so that water pollution can be reduced to some extent.
             """)
elif choice=="Water Test":
    station = st.number_input('Enter Station Number',format='%.2f')
    DO = st.number_input('Enter Dissolved Oxygen Value',format='%.2f')
    PH = st.number_input('Enter PH Value',format='%.2f')
    CM = st.number_input('Enter Carbon Monoxide Value',format='%.2f')
    BOD = st.number_input('Enter Biochemical Oxygen Demand Value',format='%.2f')
    Sodium = st.number_input('Enter Sodium Value',format='%.2f')
    TM = st.number_input('Enter Technetium Value',format='%.2f')
    if st.button('Predict'):
        result_array =[station,DO,PH,CM,BOD,Sodium,TM]
        data = np.array([result_array])
        Pre =rr.predict(data)
        output=Pre[0]
        st.markdown("THE WATER QUALITY INDEX VALUE IS :")
        st.markdown(output)
        if(output>80 and output<=100):
            st.info("poor WQI")
        elif(output>50 and output<=80):
            st.info("Low WQI")
        elif(output>20 and output<=50):
            st.info("Good WQI")
        else:
            st.info("Excellent WQI")
            
    
    
    
    