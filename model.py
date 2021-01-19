import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

df = pd.read_csv("processed_df.csv")
X= df.drop('price', axis=1)
y= df['price']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=10)
  
###### Load Model
 
model = joblib.load('model.pkl')
 
 
# it help to get predicted value of house  by providing features value 
def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]
