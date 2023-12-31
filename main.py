import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter the desired location for forecasting",
                      key="forcast place")
days = st.slider(label="forecast days", min_value=1, max_value=5, key="forecast days",
                 help="Select the number of forecasted days")

option = st.selectbox("Select the date to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = backend.getData(place, days, option)
def get_data(days):
    dates = ["2022-4-10", "2022-6-10", "2022-10-10"]
    temperatures = [10, 25, 12]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures(c)"})
st.plotly_chart(figure)
