import pandas as pd
import numpy as np


def preprocess():
    
    # Open the file with the training data.
    file = ('houses.csv')
    df = pd.read_csv(file)
    
    #drop unneeded columns.
    df.drop(['Unnamed: 0','Furnished','Terrace orientation','Garden orientation'
             ,'Number of facades'],axis =1, inplace=True)
    
    # Clean data by narrowing down options, as to avoid to small sample sets 
    # disturbing the model.
        
        # Remove group sales of houses.
    df = df[df["Property type"]== "HOUSE"]
    
        # Simplify types of houses by redefining and removing
    df = df.replace({'Property subtype' : {'BUNGALOW':'HOUSE', 'TOWN_HOUSE': 'HOUSE',
                                           'COUNTRY_COTTAGE': 'HOUSE',
                                           'CHALET':'HOUSE','COUNTRY_COTTAGE':'HOUSE'}}
                    , regex=True)
    
    df = df[~df["Property subtype"].isin(["APARTMENT_BLOCK","CASTLE",
                                          "EXCEPTIONAL_PROPERTY","HOUSE_GROUP",
                                          "OTHER_PROPERTY","MANOR_HOUSE"])]
    
        # We only want type of sale residential sale.
    df = df[df["Type of sale"]== "residential_sale"]
    
        # Some outliers with to many rooms or full apartment complexes with 50+
        # rooms and some houses with 0 bedrooms.
        # To avoid wrong results we limit the number of bedrooms
    df = df[(df["Number of bedrooms"]<10) & df["Number of bedrooms"]>0 ]
        
        # Some properties have land surfaces of 40000+m², removing these 
        # outliers and capping the max m².
    df = df[df["Surface area land"]< 5000]
        
        # Simplify if the kitchen is equipped with a simple yes/no
    df = df.replace({'Kitchen' : {'USA_HYPER_EQUIPPED':True,'USA_INSTALLED':True,
                                  'USA_SEMI_EQUIPPED':True,'USA_UNINSTALLED':False,
                                  'INSTALLED':True,'Unknown':False,'SEMI_EQUIPPED':False
                                  ,'HYPER_EQUIPPED':True,'NOT_INSTALLED':False, np.nan:False}}
                    , regex=True)
        
        # Change unknowns to False for Terrace and Garden
    df = df.replace({'Terrace' : {'Unknown':'False'}}, regex=True)
    df = df.replace({'Garden' : {'Unknown':'False'}}, regex=True)
        
        # Change NaN to False for Pool.
    df = df.replace({'Pool' : {np.nan:'False'}}, regex=True)
        
        # Many types of conditions, some with the same meaning. Narrow it down 
        # to True = Good and False = To be renovated.
    df = df.replace({'Condition' : {'GOOD':False, 'AS_NEW':False, 'JUST_RENOVATED':False,
                                    'TO_RENOVATE': True,'TO_BE_DONE_UP':True,
                                    'Unknown':True,'TO_RESTORE':True, np.nan:True, }}
                    , regex=True)
        
        # Drop row in the following columns that have NaN's since we can't 
        # really replace it with a good guess.
    df.dropna(subset=['Price', 'Number of bedrooms','Living area'], inplace=True)
    
        # Our index is messed up so we reset it first.
    df.reset_index(inplace=True)
    
        # we change all the yes/no and True/False data we put in earlier to dummies.
    df = pd.get_dummies(df, columns=['Property subtype','Kitchen','Open fireplace'
                                     ,'Terrace','Garden','Pool','Condition'])
    
        # We drop the columns that we don't need and all the False dummy columns.
    df.drop(['Property type','Type of sale','index','Kitchen_False','Open fireplace_False'
             ,'Terrace_False','Garden_False','Pool_False','Condition_False']
            ,axis =1, inplace=True)
    
        # We rename the True columns to look better.
    df.rename(columns= {'Kitchen_True':'Kitchen equipped','Open fireplace_True':'Open fireplace'
                        ,'Terrace_True':'Terrace','Garden_True':'Garden','Pool_True':'Pool'
                        ,'Condition_True':'Condition'}
              , inplace = True)
    
    # Saving it to a new csv.
    df.to_csv('houses_filtered.csv', index = False)