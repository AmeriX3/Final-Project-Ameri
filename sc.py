import numpy as np 
import pandas as pd 
from sklearn.tree import ExtraTreeRegressor
from sklearn.model_selection import train_test_split

cars= pd.read_csv("cars.csv")
cars.drop(columns="Unnamed: 0",inplace=True)

cars.reset_index(drop=True,inplace=True)
carsd = pd.get_dummies(cars)
x=carsd.drop(columns="car_price")
y=carsd["car_price"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.1)
predictor = ExtraTreeRegressor()
predictor.fit(xtrain, ytrain)

def Brands():
    
    lis= cars["car_brand"].unique()
    lis.sort()
   
    lis = tuple(lis)
    return lis

def Models(s):
    if s:
        
        lis= cars[cars["car_brand"]==s]["car_model"].unique()
        lis.sort()
        lis = tuple(lis)
        return lis
    

def Years(s):
    
        
    lis= cars[cars["car_model"]==s]["car_year"].unique()
    lis.sort()
    lis = tuple(lis)
    return lis
    
def Doors(s):
    if s:
        
        lis= cars[cars["car_model"]==s]["car_doors"].unique()
        lis.sort()
        lis = tuple(lis)
        return lis

def Price(m,b,d,y,o):
    cars= pd.read_csv("cars.csv")
    cars.drop(columns="Unnamed: 0",inplace=True)
   
    cars.reset_index(drop=True,inplace=True)
    p=0
    cars.loc[len(cars.index)]=[m, b, d, y, o,p]
    cars = pd.get_dummies(cars)
    cars2=cars[cars["car_price"]==0]  
    p = predictor.predict(cars2.drop(columns="car_price"))
    return p
