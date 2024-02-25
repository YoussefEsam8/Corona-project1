import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.header("Data analysis of the Corona virus")
st.write("")
st.write("")

data = pd.read_csv("newdf.csv")


c1,c2=st.columns(2)
c1.metric("number of Fatalities:",data['Fatalities'].sum())
c2.metric("number of ConfirmedCases:",data['ConfirmedCases'].sum())

scatter=px.scatter(data, x="ConfirmedCases", y = "Fatalities" ,color='Country/Region', template = 'plotly_dark',width = 1000, height = 900 )
st.plotly_chart(scatter)












