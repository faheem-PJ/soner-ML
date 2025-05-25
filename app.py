import joblib
import streamlit as st
import numpy as np
sv = joblib.load('final.pkl')

a1 = st.number_input("de vai")

arr = []

for i in range(59):
    arr.append(a1)


arr = np.array(arr)
arr = arr.reshape(1,-1)


if st.button("chapen vai"):

    prediction = sv.predict(arr)
    st.write(prediction)