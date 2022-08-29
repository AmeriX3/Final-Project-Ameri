
import streamlit as st
import sc 

brand = st.selectbox(
     'Select car Brand',
     sc.Brands())

model = st.selectbox("Select Model",
sc.Models(brand)
)
year = st.selectbox("Select year",sc.Years(model))

doors = st.selectbox("Select amount of doors",sc.doors(model))

odo= st.slider("Select Mileage (km)",0,100000,step=1000)

st.metric(label="Price", value=sc.Price(model,brand,doors,year,odo))

