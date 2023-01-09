from json import loads
from requests import request
from datetime import datetime
from typing import List, Any
from settings import API_TOKEN


url = "https://yahoo-weather5.p.rapidapi.com/weather"


def do_request(location: str|dict) -> dict | None:
	"""
	Function used to get response from API.
	"""

	if isinstance(location, str) and not location[0].isdigit():

		querystring = {"location": location, "format": "json", "u": "c"}

	elif isinstance(location, dict):

		querystring = {"lat": str(location.get('lat')), "long": str(location.get('let')), "format": "json", "u": "c"}

	else:

		querystring = {"woeid": location, "format": "json", "u": "c"}

	headers = {
		"X-RapidAPI-Key": API_TOKEN,
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}

	response = request("GET", url, headers=headers, params=querystring)

	if response.status_code == 200:

		return loads(response.text)

	else:

		return None


def get_forecast(response: dict) -> List[dict] | None:
	"""
	Function to get forecast from response.
	Also makes date comfortable to read.
	"""

	if isinstance(response, dict):

		forecast = response.get('forecasts')

		for i_day in forecast:

			normal_date = datetime.fromtimestamp(i_day.get('date')).date()
			i_day['date'] = str(normal_date)

		return forecast

	else:

		return None


def get_current_weather(response: dict) -> Any:
	"""
	Function to get current state of weather from response.
	"""

	if isinstance(response, dict):

		return response.get('current_observation')   # contains 5 items more

	else:

		return None



position = 'Czestochowa'

print(get_forecast(do_request(position)))


