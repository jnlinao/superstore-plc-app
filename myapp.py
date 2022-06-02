import streamlit as st
import pandas as pd
import pickle

import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.title('Superstore Sales')
st.header('BANA 290')
st.markdown('Web App - System Implementation')
st.markdown('Developed by Jacob Linao, Alexandra Currier, Harrison Lin, Jiwon Ko, Michelle Ng, Yasamin Ehteshami')


#Reading in data and displaying df
df = pd.read_csv('superstore_data3.csv')
st.header("Data Snapshot")  # add a title
st.write(df.head())  # visualize my dataframe in the Streamlit app

st.markdown('##')


#Data Cleaning
df = df.rename(columns={'Sub-Category': 'SubCategory'})

#Anova
st.header('ANOVA')

option = st.selectbox(
     'Choose Dependent Variable for Profit',
     ('SubCategory', 'Category'))

st.write('You selected:', option)

if option == 'SubCategory':
    mod1 = ols('Profit ~ SubCategory', data = df).fit()
    aov_table1 = sm.stats.anova_lm(mod1, typ=2)
    st.write(aov_table1)
    
else:
    mod1 = ols('Profit ~ Category', data = df).fit()
    aov_table2 = sm.stats.anova_lm(mod1, typ=2)
    st.write(aov_table2)

st.markdown('##')


#Linear Regression
st.header('Linear Regression')
st.markdown('Predicting Profit: Modify Dependent Features Using Slide Bars on left panel!')

from utils import user_input_features as uif

with open('final_model.pickle', 'rb') as f: 
    model = pickle.load(f)

new_x_test = uif()

new_y_prediction =  model.predict(new_x_test)
st.write(new_x_test)
st.subheader('Profit Prediction:')
st.write(round(new_y_prediction[0],2))

st.markdown('##')

#Logistic Regression
st.header('Logistic Regression')
st.markdown('Classification Model to predict whether or not a purchase will bring in above average profit.')
st.markdown('Modify independent variables to predict binary outcome of 1 (profit will be above average) or 0 (below average).')
st.markdown('##')

from utils import user_input_features_2 as uif2

with open('final_model_logreg.pickle', 'rb') as f: 
    log_reg_model = pickle.load(f)

new_x_test_2 = uif2()
new_y_prediction_2 =  log_reg_model.predict(new_x_test_2)

st.subheader('Model Prediction')
if new_y_prediction_2 == 1:
    st.write('Predicted Profit is above average!')
else: 
    st.write('Predicted Profit is below average!')


