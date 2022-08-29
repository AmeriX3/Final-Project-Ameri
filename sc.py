import numpy as np 
import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

cars= pd.read_csv("cars.csv")
carsd = pd.get_dummies(cars)
x=carsd.drop(columns="car_price")
y=carsd["car_price"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
predictor = DecisionTreeRegressor()
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
    else:
        
        lis= cars["car_model"].unique()
        lis.sort()
        lis = tuple(lis)
        return lis

def Years(s):
    if s:
        
        lis= cars[cars["car_model"]==s]["car_year"].unique()
        lis.sort()
        lis = tuple(lis)
    else:
        
        lis= cars["car_year"].unique()
        lis.sort()
        lis = tuple(lis)
        return lis

def Doors(s):
    if s:
        
        lis= cars[cars["car_model"]==s]["car_door"].unique()
        lis.sort()
        lis = tuple(lis)
        return lis

def Price(m,b,d,y,o):
    
    dic = {"car_model": m,"car_brand": b,"car_doors": d,
       "car_year":y, "car_odo":o}
    df = pd.DataFrame.from_dict(dic)
    p = predictor.predict(df)
    return p

