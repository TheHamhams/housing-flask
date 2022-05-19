import streamlit as st
import pickle
import numpy as np

import datetime

date = datetime.date.today()
year = int(date.strftime("%Y"))

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
    
    neighborhoods = ('Blmngtn - Bloomington Heights',
       'Blueste	- Bluestem',
       'BrDale - Briardale',
       'BrkSide	- Brookside',
       'ClearCr	- Clear Creek',
       'CollgCr	- College Creek',
       'Crawfor	- Crawford',
       'Edwards	- Edwards',
       'Gilbert	- Gilbert',
       'IDOTRR	- Iowa DOT and Rail Road',
       'MeadowV	- Meadow Village',
       'Mitchel	- Mitchell',
       'Names	- North Ames',
       'NoRidge	- Northridge',
       'NPkVill	- Northpark Villa',
       'NridgHt	- Northridge Heights',
       'NWAmes	- Northwest Ames',
       'OldTown	- Old Town',
       'SWISU	- South & West of Iowa State University',
       'Sawyer	- Sawyer',
       'SawyerW	- Sawyer West',
       'Somerst	- Somerset',
       'StoneBr	- Stone Brook',
       'Timber	- Timberland',
       'Veenker	- Veenker')
    
    conditions = ('Norm - Normal Proximity', 
                  'Pos - Positive off-site feature: park, greenbelt, etc.',
                  'RR - Railroad')
    
    building_types = ('1Fam	- Single-family Detached',	
       '2FmCon - Two-family Conversion; originally built as one-family dwelling',
       'Duplx - Duplex',
       'TwnhsE -	Townhouse End Unit',
       'TwnhsI -	Townhouse Inside Unit',)
    
    building_styles = ('1Story	- One story',
       '1.5Fin	- One and one-half story: 2nd level finished',
       '1.5Unf	- One and one-half story: 2nd level unfinished',
       '2Story	- Two story',
       '2.5Fin	- Two and one-half story: 2nd level finished',
       '2.5Unf	- Two and one-half story: 2nd level unfinished',
       'SFoyer	- Split Foyer',
       'SLvl	- Split Level')
    
    ratings = ('10 -	Very Excellent',
       '9 -	Excellent',
       '8 -	Very Good',
       '7 -	Good',
       '6 -	Above Average',
       '5 -	Average',
       '4 -	Below Average',
       '3 -	Fair',
       '2 -	Poor',
       '1 -	Very Poor')
    
    ext1 = ('BrkFace- 	Brick Face',
       'CemntBd -	Cement Board',
       'HdBoard -	Hard Board',
       'MetalSd -	Metal Siding',
       'Other- 	Other',
       'Plywood -	Plywood',
       'PreCast -	PreCast',	
       'VinylSd -	Vinyl Siding',
       'Wd Sdng -	Wood Siding')
    
    ext2 = ('CemntBd -	Cement Board',
       'HdBoard -	Hard Board',
       'MetalSd -	Metal Siding',
       'Other -	Other',
       'Plywood -	Plywood',
       'PreCast -	PreCast',	
       'VinylSd -	Vinyl Siding',
       'Wd Sdng -	Wood Siding')
    
    veneers = ('BrkCmn -	Brick Common',
       'BrkFace -	Brick Face',
       'CBlock -	Cinder Block',
       'None -	None',
       'Stone -	Stone')
    
    ex_po = ('Ex -	Excellent',
       'Gd -	Good',
       'TA -	Average/Typical',
       'Fa -	Fair',
       'Po -	Poor',
       'NA')
    
    height_ex_po = ('Ex -	Excellent (100+ incehs)',
       'Gd -	Good (90-99 inches)',
       'TA -	Average/Typical (80-89 inches)',
       'Fa -	Fair (70-79 incehs)',
       'Po -	Poor (<70 inches)',
       'NA')
    
    foundations = ('BrkTil -	Brick & Tile',
       'CBlock -	Cinder Block',
       'PConc -	Poured Contrete',	
       'Other - Other')
    
    
    # App Selectors
    
    MSSubClass = st.selectbox('What type of dwelling is the home?', dwellings)
    MSSubClass = int(MSSubClass.split()[0])
    
    MSZoning = st.checkbox('Is the dwelling zoning "RL: Residential Low Density"?')
    binary(MSZoning)
    
    LotFrontage = st.slider('How many feet of street is connected to the property?', 0, 500, 60)
    
    LotArea = st.number_input('How many square feet is the lot size?', 0, 250000)
    
    Alley = st.checkbox('Is there paved alley access to the property?')
    binary(Alley)
    
    LotShape = st.checkbox('Does the property have a regular shape?')
    binary(LotShape)
    
    LotConfig = st.selectbox('What is the lot configuration?', lot_configs)
    LotConfig = LotConfig.split()[0]
    
    LandSlope = st.checkbox('Does the property only have a gentle slope?')
    binary(LandSlope)
    
    Neighborhood = st.selectbox('What neighborhood is the property located in?', neighborhoods)
    Neighborhood = Neighborhood.split()[0]
    
    Condition1 = st.selectbox('What features does the property have close proximity to?', conditions)
    Condition1 = Condition1.split()[0]
    
    Condition2 = st.checkbox('Does the property proximity to more than one of the above features?')
    if Condition2 == True:
        Condition2 = 0
    else:
        Condition2 = 1
    
    BldgType = st.selectbox('What is the type of dwelling?', building_types).split()[0]
    
    HouseStyle = st.selectbox('What is the style of the dwelling?', building_styles).split()[0]
    
    OverallQual = st.selectbox('What is the quality of th overall material and finish of the dwelling?', ratings).split()[0]
    
    OverallCond = st.selectbox('What is the overall condition of the dwelling?', ratings).split()[0]
    
    age = st.number_input('What year was the house built?')
    Year_Old = year - age    
    
    remod = st.number_input('Remodel date (same as construction date if no remodeling or additions)')
    Remod_Age = year - remod   
    
    Gable_Roof = st.checkbox('Does the house have a gable roof?')
    binary(Gable_Roof)
    
    Comp_Roof = st.checkbox('Is the roof material Standard (Composite) Shingle?')
    binary(Comp_Roof)
    
    Exterior1st = st.selectbox('Exterior covering on house', ext1).split()[0]
    
    Exterior2nd = st.selectbox('Exterior covering on house (if more than one material)', ext2).split()[0]
    
    MasVnrType = st.selectbox('Masonty veneer type', veneers).split()[0]
    
    MasVnrArea = st.number_input('Masonry veneer area in square feet')
    
    ExterQual = st.selectbox('Quality of materials on the exterior', ex_po).split()[0]
    
    ExterCond = st.selectbox('Present condition of the material on the exterior', ex_po).split()[0]
    
    Foundation = st.selectbox('Type of foundation', foundations).split()[0]
    
    BsmtQual = st.selectbox('Evaluate the height of the basement', height_ex_po).split()[0]
    
    BsmtCond = st.selectbox('What is the general condition of the basement?', ex_po).split()[0]
    
    