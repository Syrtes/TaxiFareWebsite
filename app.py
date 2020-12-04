import streamlit as st
import pandas as pd
import numpy as nbpass
import datetime
import requests

'''
# Taxi Fare Prediction front
'''
st.write("Please input the ride details")

d3 = st.date_input("Travel Date")
h1 = st.time_input("Travel Hour")
plong = st.number_input('Pickup Longitude',-73.950655)
plat = st.number_input('Pickup Latitude',40.783282)
dlong = st.number_input('Dropoff Longitude',-73.984365)
dlat = st.number_input('Dropoff Latitude',40.769802)
nbpass = st.number_input("Passenger Count", min_value=1, max_value=8)



url = 'http://localhost:8000/predict_fare/'



X = dict(
        key=1,
        pickup_datetime = f'{d3} {h1}UTC',
        pickup_longitude=plong,
        pickup_latitude=plat,
        dropoff_longitude=dlong,
        dropoff_latitude=dlat,
        passenger_count=nbpass)




response = requests.get(url, params=X).json()

st.header("Prediction")
st.write("Price:",round(response['prediction'],0),"USD")

