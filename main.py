
import streamlit as st
import sc 

if 'brand' not in st.session_state:
    st.session_state['key'] = 'brand'
def modelS():
     if st.session_state["model"]:
          st.session_state["key"]= st.session_state["model"]

def brandS():
     if st.session_state["brand"]:
          st.session_state["key"]= st.session_state["brand"]
def doneS():
     if st.session_state["done"]:
          st.session_state["key"]= st.session_state["done"]


brand = st.selectbox(    
               'Select car Brand',
               sc.Brands(),on_change=brandS,key='brand')


if st.session_state['brand']:

    model = st.selectbox("Select Model",sc.Models(brand),on_change=modelS,key="model")
   

if st.session_state['model']:
     year = st.selectbox("Select year",sc.Years(model))
     

     doors = st.selectbox("Select amount of doors",sc.Doors(model))
     odo= st.slider("Select Mileage (km)",0,100000,step=1000,on_change=doneS,key='done')
     

if st.session_state["done"]:

     st.metric(label="Price", value=sc.Price(model,brand,doors,year,odo))


