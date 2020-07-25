from flask import Flask, request
import os
import requests

app = Flask(__name__)

url = "https://community-open-weather-map.p.rapidapi.com/weather"

@app.route('/', methods=["GET"])
def get_status():
    if request.method == "GET":
        return 'Healthy'


@app.route('/weather/v1', methods=["POST"])
def get_weather():

    city_name = request.get_data()
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get("API_KEY"),
    }
    querystring = {"callback": "test", "id": os.environ.get("SERVICE_ID"), "units": "metric", "mode": "xml",
                   "q": city_name}
    response = requests.request("POST", url, headers=headers, params=querystring).json()
    response["version"] = "1.0"
    response["deploy_color"] = os.environ.get("DEPLOY_COLOR")

    return str(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
