import streamlit as st
import numpy as np
from lifexp.pipeline.prediction import PredictionPipeline
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


# Define the Streamlit app
def main():
    st.title("Life Expectancy Prediction")

    # Create input widgets for user to enter data
    Country = st.selectbox("Status", ['India','Afghanistan'])
    Year = st.selectbox("Year", ['2000','2001','2002','2003','2004','2005','2006','2007',
                                 '2008','2009','2010','2011','2012','2013','2014','2015'])
    Status = st.selectbox("Status", ['Developing','Developed'])
    Adult_Mortality= st.number_input("Adult Mortality", min_value=0, max_value=500, step=1)
    infant_deaths=st.number_input('infant deaths',min_value=0, max_value=500, step=1)
    Alcohol=st.number_input('Alcohol',min_value=0.0, max_value=500.00, step=0.01)
    percentage_expenditure=st.number_input('percentage expenditure',min_value=0.0, max_value=500.00000, step=0.00001)
    Hepatitis_B=st.number_input('Hepatitis B',min_value=0, max_value=500, step=1)
    Measles=st.number_input('Measles',min_value=0, max_value=10000, step=1)
    BMI=st.number_input('BMI',min_value=0.0, max_value=50.00, step=.001)
    under_five_deaths=st.number_input('under-five deaths',min_value=0, max_value=500, step=1)
    Polio=st.number_input('Polio',min_value=0, max_value=500, step=1)
    Total_expenditure=st.number_input('Total expenditure',min_value=0.0, max_value=500.00, step=0.01)
    Diphtheria=st.number_input('Diphtheria',min_value=0, max_value=500, step=1)
    HIV_AIDS=st.number_input('HIV/AIDS',min_value=0.0, max_value=500.00, step=0.01)
    GDP=st.number_input('GDP',min_value=0.0, max_value=10000.00000, step=0.00001)
    Population=st.number_input('Population',min_value=0, max_value=1000000, step=1)
    thinness_1_19_years=st.number_input('thinness  1-19 years',min_value=0.0, max_value=500.00, step=0.01)
    thinness_5_9_years=st.number_input('thinness 5-9 years',min_value=0.0, max_value=500.00, step=0.01)
    Income_composition_of_resources=st.number_input('Income composition of resources',min_value=0.0, max_value=500.00, step=0.01)
    Schooling=st.number_input('Schooling',min_value=0.0, max_value=500.00, step=0.01)

       
    # Add more input fields for other features...

    if st.button("Predict"):
        try:
            # Combine encoded categorical data with numeric data
            data = np.array([Country,Year,Status,Adult_Mortality,infant_deaths,Alcohol,
                             percentage_expenditure,
                             Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,
                             Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,
                             thinness_5_9_years,Income_composition_of_resources,Schooling])

            # Make a prediction using your PredictionPipeline
            obj = PredictionPipeline()
            prediction = obj.predict(data.reshape(1, -1))

            st.success(f"Predicted Quality: {prediction[0]}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
