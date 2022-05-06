import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train():
    
    # Open the file with the filtered houses
    data = pd.read_csv('../preprocessing/houses_filtered.csv')
    
    # Determine our X and y. Location is dropped for now but future implements
    # should take this into account.
    X = data.drop(['Location','Price'], axis=1)
    y = data['Price']
    
    # We split and determine test/train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                        random_state=42)
    
    # We decide on a model and fit our data to it.    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # We save our model to pickle in our model folder.
    pickle.dump(model, open('../model/model.pickle', 'wb'))

train()