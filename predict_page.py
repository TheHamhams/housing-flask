import pickle
import streamlit as st
import pandas as pd
import datetime


date = datetime.date.today()
year = int(date.strftime("%Y"))

def load_model():
   with open('model.pickle', 'rb') as file:
      data = pickle.load(file)
   return data

data = load_model()

model = data['model']
model_columns = data['cols']
sample = data['sample']

def binary(variable):
   if variable == True:
        variable = 1
   else:
        variable = 0
   return variable


def show_predict_page():
   st.title('Housing Price Prediction')
   
   st.write("""
            This data is from the Kaggle [Housing Competition](https://www.kaggle.com/competitions/home-data-for-ml-course/overview). Answer the following questions to create a housing price prediction.
            """)
   # Selection Options
   dwellings = ('20 -> 1-STORY 1946 & NEWER ALL STYLES',
                  '30 -> 1-STORY 1945 & OLDER',
                  '50 -> 1-1/2 STORY FINISHED ALL AGES',
                  '60 -> 2-STORY 1946 & NEWER',
                  '70 -> 2-STORY 1945 & OLDER',
                  '80 -> SPLIT OR MULTI-LEVE',
                  '90 -> DUPLEX - ALL STYLES AND AGES',
                  '120 -> 1-STORY PUD (Planned Unit Development) - 1946 & NEWER',
                  '150 -> 1-1/2 STORY PUD - ALL AGES',
                  '160 -> 2-STORY PUD - 1946 & NEWER',
                  'other - other')
   
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
      'Duplex - Duplex',
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
   
   ext1 = ('BrkFace - 	Brick Face',
      'CemntBd -	Cement Board',
      'HdBoard -	Hard Board',
      'MetalSd -	Metal Siding',
      'Other- 	Other',
      'Plywood -	Plywood',
      'PreCast -	PreCast',	
      'VinylSd -	Vinyl Siding',
      'Wd Sdng -	Wood Siding')
   
   ext2 = ('HdBoard -	Hard Board',
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
   
   ex_po = ('5 -	Excellent',
      '4 -	Good',
      '3 -	Average/Typical',
      '2 -	Fair',
      '1 -	Poor',
      '0 - NA')
   
   height_ex_po = ('5 -	Excellent (100+ incehs)',
      '4 -	Good (90-99 inches)',
      '3 -	Average/Typical (80-89 inches)',
      '2 -	Fair (70-79 incehs)',
      '1 -	Poor (<70 inches)',
      '0 - NA')
   
   foundations = ('BrkTil -	Brick & Tile',
      'CBlock -	Cinder Block',
      'PConc -	Poured Contrete',	
      'Other - Other')
   
   exposures = ('4 -	Good Exposure',
       '3 -	Average Exposure (split levels or foyers typically score average or above)',	
       '2 -	Mimimum Exposure',
       '1 -	No Exposure',
       '0 -	No Basement')
   
   finish_types = ('6 -	Good Living Quarters',
       '5 -	Average Living Quarters',
       '4 -	Below Average Living Quarters',
       '3 -	Average Rec Room',
       '2 -	Low Quality',
       '1 -	Unfinshed',
       '0 -	No Basement')

   functionalities = ('7 -	Typical Functionality',
       '6 -	Minor Deductions 1',
       '5 -	Minor Deductions 2',
       '4 -	Moderate Deductions',
       '3 -	Major Deductions 1',
       '2 -	Major Deductions 2',
       '1 -	Severely Damaged',
       '0 -	Salvage only')
   
   fp_ex_po = ('5 -	Excellent - Exceptional Masonry Fireplace',
       '4 -	Good - Masonry Fireplace in main level',
       '3 -	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement',
       '2 -	Fair - Prefabricated Fireplace in basement',
       '1 -	Poor - Ben Franklin Stove',
       '0 -	No Fireplace')
   
   garage_types = ('Attchd -	Attached to home',
       'BuiltIn -	Built-In (Garage part of house - typically has room above garage)',
       'Detchd -	Detached from home',
       'Other - Other',
       'None -	No Garage')
   
   garage_finishes = ('Fin -	Finished',
       'RFn -	Rough Finished',
       'Unf -	Unfinished',
       'None -	No Garage')
   
   driveways = ('2 -	Paved', 
       '1 -	Partial Pavement',
       '0 -	Dirt/Gravel')
   
   fences = ('4 -	Good Privacy',
       '3 -	Minimum Privacy',
       '2 -	Good Wood',
       '1 -	Minimum Wood/Wire',
       '0 -	No Fence')
   
   months = ('1 - January', 
             '2 - February',
             '3 - March',
             '4 - April',
             '5 - May',
             '6 - June',
             '7 - July',
             '8 - August',
             '9 - September',
             '10 - October',
             '11 - November',
             '12 - December')
   
   sales = ('WD - 	Warranty Deed - Conventional',
       'New -	Home just constructed and sold',
       'COD -	Court Officer Deed/Estate',
       'Other -	Other')
   
   sale_conditions = ('Normal -	Normal Sale',
       'Abnorml -	Abnormal Sale -  trade, foreclosure, short sale',
       'Partial -	Home was not completed when last assessed (associated with New Homes)',
       'Other - Other')
   
   # App Selectors
   
   MSSubClass = st.selectbox('What type of dwelling is the home?', dwellings).split()[0]
   
   MSZoning = st.checkbox('Is the dwelling zoning "RL: Residential Low Density"?')
   
   LotFrontage = st.slider('How many feet of street is connected to the property?', 0, 500, 60)
   
   LotArea = st.number_input('How many square feet is the lot size?', 0, 250000)
   
   Street_Pave = st.checkbox('Does the house have paved access?')
   
   Alley = st.checkbox('Is there paved alley access to the property?')
   
   LotShape = st.checkbox('Does the property have a regular shape?')
   
   LandContour_Flat = st.checkbox('IS the property near flat or level?')
   
   LotConfig = st.selectbox('What is the lot configuration?', lot_configs).split()[0]
   
   LandSlope_Gentle = st.checkbox('Does the property only have a gentle slope?')
   
   Neighborhood = st.selectbox('What neighborhood is the property located in?', neighborhoods).split()[0]
   
   Condition1 = st.selectbox('What features does the property have close proximity to?', conditions).split()[0]
   
   Condition2 = st.checkbox('Does the property proximity to more than one of the above features?')
   
   BldgType = st.selectbox('What is the type of dwelling?', building_types).split()[0]
   
   HouseStyle = st.selectbox('What is the style of the dwelling?', building_styles).split()[0]
   
   OverallQual = int(st.selectbox('What is the quality of th overall material and finish of the dwelling?', ratings).split()[0])
   
   OverallCond = int(st.selectbox('What is the overall condition of the dwelling?', ratings).split()[0])
   
   age = st.number_input('What year was the house built?')
   
   Gable_Roof = st.checkbox('Does the house have a gable roof?')
   
   Comp_Roof = st.checkbox('Is the roof material Standard (Composite) Shingle?')
   
   Exterior1st = st.selectbox('Exterior covering on house', ext1).split()[0]
   
   Exterior2nd = st.selectbox('Exterior covering on house (if more than one material)', ext2).split()[0]
   
   MasVnrType = st.selectbox('Masonty veneer type', veneers).split()[0]
   
   MasVnrArea = st.number_input('Masonry veneer area in square feet')
   
   ExterQual = int(st.selectbox('Quality of materials on the exterior', ex_po).split()[0])
   
   ExterCond = int(st.selectbox('Present condition of the material on the exterior', ex_po).split()[0])
   
   Foundation = st.selectbox('Type of foundation', foundations).split()[0]
   
   BsmtQual = int(st.selectbox('Evaluate the height of the basement', height_ex_po).split()[0])
   
   BsmtCond = int(st.selectbox('What is the general condition of the basement?', ex_po).split()[0])
   
   BsmtExposure = st.selectbox('Refers to walkout or garden level walls', exposures).split()[0]
   
   BsmtFinType1 = int(st.selectbox('Rating of basement finished area', finish_types).split()[0])
   
   BsmtFinSF1 = st.number_input('Finished area square feet')
   
   BsmtFinType2 = int(st.selectbox('Rating of basement finished area (if multiple types)', finish_types).strip()[0])
   
   BsmtFinSF2 = st.number_input('Second finished area square feet')
   
   BsmtUnfSF = st.number_input('Unifinished square feet of basement area')
   
   Gas = st.checkbox('Does the house have gas heating?')
   
   HeatingQC = int(st.selectbox('Heating quality and condition', ex_po).split()[0])
   
   CentralAir = st.checkbox('Does the house have central air conditioning?')
   
   SecondFlrSF = st.number_input('What is the square feet of the second floor?')
   
   Electrical = st.checkbox('Does the electrical system use standard circut breakers and Romex?')
   
   LowQualFinSF = st.number_input('How much of the square feet of the house includes low quality finishing?')
   
   GrLivArea = st.number_input('Above grade (ground) living area square feet')
   
   BsmtFullBath = st.slider('How many basement full bathrooms are present?', 0, 3)
   
   BsmtHalfBath = st.slider('How many basement half bathrooms are present?', 0, 2)
   
   FullBath = st.slider('How many full bathrooms above grade are present?', 0, 3)
   
   HalfBath = st.slider('How many half bathrooms above grade are present?', 0, 2)
   
   BedroomAbvGr = st.slider('How many bedrooms above grade are present?', 0, 8)
   
   KitchenAbvGr = st.slider('How many kitches above grade are present?', 0, 3)
   
   KitchenQual = int(st.selectbox('What is the quality of the kitchen?', ex_po).split()[0])
   
   Functional = int(st.selectbox('Home functionality (Assume typical unless deductions are warranted)', functionalities).split()[0])
   
   Fireplaces = st.slider('How many fireplaces are present?', 0, 3)
   
   FireplaceQu = int(st.selectbox('What is the quality of the fireplaces?', fp_ex_po).split()[0])
   
   GarageType = st.selectbox('Garage location', garage_types).split()[0]
   
   GarageFinish = st.selectbox('Interior finish of the garage.', garage_finishes).split()[0]
   
   GarageCars = st.slider('Garage car capacity', 0, 4)
   
   GarageQual = int(st.selectbox('Garage quality', ex_po).split()[0])
   
   GarageCond = int(st.selectbox('Garage condition', ex_po).split()[0])
   
   PavedDrive = int(st.selectbox('How paved is the driveway?', driveways).split()[0])
   
   WoodDeckSF = st.number_input('How many square feet of wood deck area are present?')
   
   OpenPorchSF = st.number_input('How many square feet pf open porch are present?')
   
   EnclosedPorch = st.number_input('How many square feet of enclosed porch are present?')
   
   ThreeSsnPorch = st.number_input('How many square feet of three season porch area are present?')
   
   ScreenPorch = st.number_input('How many square feet of screen porch area are present?')
   
   PoolArea = st.number_input('How many square feet of pool area are present?')
   
   MiscFeature = st.checkbox('Does the house include a feature not covered? (Elevator, 2nd Garage, Shed, etc.)')
   
   MiscVal = st.number_input('What is the value of the above feature?')
   
   MoSold = int(st.selectbox('What month was the property sold?', months).split()[0])
   
   sage = st.slider('What year was the property sold?', 1990, 2010)
   
   SaleType = st.selectbox('What was the type of sale?', sales).split()[0]
   
   SaleCondition = st.selectbox('What was the sale condition?', sale_conditions).split()[0]
   
   # Button to create prediction

   predict_button = st.button('Predict House Price')
   
   if predict_button:
  
 
      MSZoning = binary(MSZoning)
      Street_Pave = binary(Street_Pave)
      Alley = binary(Alley)
      LotShape = binary(LotShape)
      LandContour_Flat = binary(LandContour_Flat)
      LandSlope_Gentle = binary(LandSlope_Gentle)
      if Condition2 == True:
         Condition2 = 0
      else:
         Condition2 = 1
      Year_Old = year - age
      #Remod_Age = year - remod
      Gable_Roof = binary(Gable_Roof)
      Comp_Roof = binary(Comp_Roof)
      Gas = binary(Gas)
      CentralAir = binary(CentralAir)
      Electrical = binary(Electrical)
      MiscFeature = binary(MiscFeature)
      SaleAge = year - sage
      
      # Create prediction DataFrame
   
      df_dict = {f'MSSubClass_{MSSubClass}': 1, 'MSZoning': MSZoning, 'LotFrontage': LotFrontage, 'LotArea': LotArea, 'Street_Pave': Street_Pave,
               'LotShape': LotShape, 'LandContour_Flat': LandContour_Flat, f'LotConfig_{LotConfig}': 1, 'LandSlope_Gentle': LandSlope_Gentle,
              f'Neighborhood_{Neighborhood}': 1, f'Condition1_{Condition1}':1, 'Condition2': Condition2, f'BldgType_{BldgType}': 1, f'HouseStyle_{HouseStyle}': 1,
              'OverallQual': OverallQual, 'OverallCond': OverallCond, 'Year_Old': Year_Old, 'Gable_Roof': Gable_Roof,
              'Comp_Roof': Comp_Roof, f'Exterior1st_{Exterior1st}': 1, f'Exterior2nd_{Exterior2nd}': 1, f'MasVnrType_{MasVnrType}': 1, 'MasVnrArea': MasVnrArea,
              'ExterQual': ExterQual, 'ExterCond': ExterCond, f'Foundation_{Foundation}': 1, 'BsmtQual': BsmtQual, 'BsmtCond': BsmtCond,
              'BsmtExposure': BsmtExposure, 'BsmtFinType1': BsmtFinType1, 'BsmtFinSF1': BsmtFinSF1, 'BsmtFinType2': BsmtFinType2,
              'BsmtFinSF2': BsmtFinSF2, 'BsmtUnfSF': BsmtUnfSF, 'Gas': Gas, 'HeatingQC': HeatingQC, 'CentralAir': CentralAir, 
              '2ndFlrSF': SecondFlrSF, 'Electrical': Electrical, 'LowQualFinSF': LowQualFinSF, 'GrLivArea': GrLivArea, 'BsmtFullBath': BsmtFullBath,
              'BsmtHalfBath': BsmtHalfBath, 'FullBath': FullBath, 'HalfBath': HalfBath, 'BedroomAbvGr': BedroomAbvGr, 'KitchenAbvGr': KitchenAbvGr,
              'KitchenQual': KitchenQual, 'Functional': Functional, 'Fireplaces': Fireplaces, 'FireplaceQu': FireplaceQu, f'GarageType_{GarageType}': 1,
              f'GarageFinish_{GarageFinish}': 1, 'GarageCars': GarageCars, 'GarageQual': GarageQual, 'GarageCond': GarageCond, 'PavedDrive': PavedDrive,
              'WoodDeckSF': WoodDeckSF, 'OpenPorchSF': OpenPorchSF, 'EnclosedPorch': EnclosedPorch, '3SsnPorch': ThreeSsnPorch,
              'ScreenPorch': ScreenPorch, 'PoolArea': PoolArea, 'MiscVal': MiscVal,
              'MoSold': MoSold, 'SaleAge': SaleAge, f'SaleType_{SaleType}': 1, f'SaleCondition_{SaleCondition}': 1}
   
      
      df = pd.DataFrame([df_dict])

      # Make df same dimensions as model 
      
      missing_cols = []
      
      for column in model_columns:
         if column not in df.columns:
            missing_cols.append(column)
      
      for column in missing_cols:
         df.insert(0, column, 0)
         
      df = df.reindex(sample.columns, axis=1)
      # Make prediction
      
      def predicter(data):
         m = model.predict(data)
         return m 
      result = predicter(df)
      
      st.success(f'Predicted house price is {result[0]}')
      
      #df.to_csv('text.csv', index=False)