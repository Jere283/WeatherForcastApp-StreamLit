import requests
API_KEY="f3aa63fefd87bea760a10f6052a5d54b"

def getData(place, forecast_days=None, forecast_type=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # filter the data so it can show the data based on the days selected
    filtered_data = data["list"]
    data_for_days = forecast_days*8
    filtered_data = filtered_data[:data_for_days]

    if forecast_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]

    if forecast_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(getData(place="Tegucigalpa", forecast_days=3, forecast_type="Sky"))
