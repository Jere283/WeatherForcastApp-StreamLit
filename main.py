import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter the desired location for forecasting",
                      key="forcast place")
days = st.slider(label="forecast days", min_value=1, max_value=5, key="forecast days",
                 help="Select the number of forecasted days")

option = st.selectbox("Select the date to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

st.line_chart()
