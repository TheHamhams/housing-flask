import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model.pickle', 'rb') as file:
        data = pickle.load(file)
    return data

#data = load_model()

#model = data['model']

def binary(variable):
    if variable == True:
        variable = 1
    else:
        variable = 0


def show_predict_page():
    st.title('Housing Price Prediction')
    
    
    # Selection Options
    dwellings = ('20 -> 1-STORY 1946 & NEWER ALL STYLES',
                    '30 -> 1-STORY 1945 & OLDER',
                    '40 -> 1-STORY W/FINISHED ATTIC ALL AGES',
                    '45 -> 1-1/2 STORY - UNFINISHED ALL AGES',
                    '50 -> 1-1/2 STORY FINISHED ALL AGES',
                    '60 -> 2-STORY 1946 & NEWER',
                    '70 -> 2-STORY 1945 & OLDER',
                    '75 -> 2-1/2 STORY ALL AGES',
                    '80 -> SPLIT OR MULTI-LEVE',
                    '85 -> SPLIT FOYER',
                    '90 -> DUPLEX - ALL STYLES AND AGES',
                    '120 -> 1-STORY PUD (Planned Unit Development) - 1946 & NEWER',
                    '150 -> 1-1/2 STORY PUD - ALL AGES',
                    '160 -> 2-STORY PUD - 1946 & NEWER',
                    '180 -> PUD - MULTILEVEL - INCL SPLIT LEV/FOYER',
                    '190 -> 2 FAMILY CONVERSION - ALL STYLES AND AGES')
    
    lot_configs = ('Inside - Inside lot',
                        'Corner	- Corner lot',
                        'CulDSac - Cul-de-sac',
                        'Other')
    
    
    # App Selectors
    
    MSSubClass = st.selectbox('What type of dwelling is the home?', dwellings)
    MSSubClass = int(MSSubClass.strip()[0])
    
    MSZoning = st.checkbox('Is the dwelling zoning "RL: Residential Low Density"?')
    binary(MSZoning)
    
    LotFrontage = st.slider('How many feet of street is connected to the property?', 0, 500, 60)
    
    LotArea = st.number_input('How many square feet is the lot size?', 0, 250000)
    
    Alley = st.checkbox('Is there paved alley access to the property?')
    binary(Alley)
    
    LotShape = st.checkbox('Does the property have a regular shape?')
    binary(LotShape)
    
    LotConfig = st.selectbox('What is the lot configuration?', lot_configs)
    LotConfig = LotConfig.strip()[0]