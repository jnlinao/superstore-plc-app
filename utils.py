import pandas as pd
import numpy as np
import streamlit as st


def user_input_features():
    ShipMode_SameDay = st.sidebar.slider('ShipMode_SameDay', 0,1)
    ShipMode_StandardClass = st.sidebar.slider('ShipMode_StandardClass', 0,1)
    ShipMode_FirstClass = st.sidebar.slider('ShipMode_FirstClass', 0,1)
    ShipMode_SecondClass = st.sidebar.slider('ShipMode_SecondClass', 0,1)
    Segment_Consumer = st.sidebar.slider('Segment_Consumer', 0,1)
    Segment_Corporate = st.sidebar.slider('Segment_Corporate', 0,1)
    Segment_HomeOffice = st.sidebar.slider('Segment_HomeOffice', 0,1)
    Region_Central = st.sidebar.slider('Region_Central', 0,1)
    Region_East = st.sidebar.slider('Region_East', 0,1)
    Region_South = st.sidebar.slider('Region_South', 0,1)
    Region_West = st.sidebar.slider('Region_West', 0,1)
    Category_Furniture = st.sidebar.slider('Category_Furniture', 0,1)
    Category_OfficeSupplies = st.sidebar.slider('Category_OfficeSupplies', 0,1)
    Category_Technology = st.sidebar.slider('Category_Technology', 0,1)
    Quantity = st.sidebar.slider('Quantity', 0,10,2)
    Discount = st.sidebar.slider('Discount', 0.0,0.5,0.1)
    Mean = st.sidebar.slider('Mean', 0,100000,10000)
    Median = st.sidebar.slider('Median', 0,100000,10000)
    Cost_Per_Unit = st.sidebar.slider('Cost_Per_Unit', 0,100,20)
    Profit_Per_Unit = st.sidebar.slider('Profit_Per_Unit', 5,100,25)

    
    data = [[ShipMode_SameDay, ShipMode_StandardClass, ShipMode_FirstClass, ShipMode_SecondClass, 
            Segment_Consumer, Segment_Corporate, Segment_HomeOffice, Region_Central, 
            Region_East, Region_South, Region_West, Category_Furniture,
            Category_OfficeSupplies, Category_Technology, Quantity, Discount,
            Mean, Median, Cost_Per_Unit, Profit_Per_Unit]]  
    
    features = pd.DataFrame(data, columns = ['Ship Mode-Same Day', 'Ship Mode-Standard Class',
       'Ship Mode-First Class', 'Ship Mode-Second Class', 'Segment-Consumer',
       'Segment-Corporate', 'Segment-Home Office', 'Region-Central',
       'Region-East', 'Region-South', 'Region-West', 'Category-Furniture',
       'Category-Office Supplies', 'Category-Technology', 'Quantity',
       'Discount', 'Mean', 'Median', 'Cost_Per_Unit', 'Profit_Per_Unit'])

    return features

def user_input_features_2():

    quantity = st.slider('Quantity', 0, 14, 2)
    discount = st.slider('Discount', 0.0,.8,.1)
    cost = st.slider('Cost', 10,200,20)
    sc_bookcases = st.slider('Sub-Category_Bookcases',0,1)
    sc_chairs = st.slider('Sub-Category_Chairs',0,1)
    sc_envelopes = st.slider('Sub-Category_Envelopes',0,1)
    sc_labels = st.slider('Sub-Category_Labels',0,1)
    sc_machines = st.slider('Sub-Category_Machines',0,1)
    sc_paper = st.slider('Sub-Category_Paper',0,1)
    sc_storage = st.slider('Sub-Category_Storage',0,1)
    sc_supplies = st.slider('Sub-Category_Supplies',0,1)
    furniture = st.slider('Category Furniture',0,1)
    officesupplies = st.slider('Category Office Supplies',0,1)

    user_input_data = [[quantity, discount, cost, sc_bookcases, sc_chairs, sc_envelopes, sc_labels, sc_machines, 
                            sc_paper, sc_storage, sc_supplies, furniture, officesupplies]]

    new_x_test = pd.DataFrame(user_input_data, columns = ['Quantity', 'Discount', 'Cost', 'Sub-Category_Bookcases',
       'Sub-Category_Chairs', 'Sub-Category_Envelopes', 'Sub-Category_Labels',
       'Sub-Category_Machines', 'Sub-Category_Paper', 'Sub-Category_Storage',
       'Sub-Category_Supplies', 'Category_Furniture',
       'Category_Office Supplies'])

    return new_x_test 

