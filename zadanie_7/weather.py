import json
import requests
import sys
import time
from datetime import datetime
from datetime import timedelta

class Weather:

	class my_exception(Exception):
		def __init__(self):
			print("Nie wiem\n")

	def __init__(self, args):
		if len(args) == 2:
			self.key, self.date2check = args
		elif len(args) == 1:
			self.key, self.date2check = args[0], (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
		self.today = datetime.now().strftime('%Y-%m-%d')
		self.lat = "51.79918186247448"
		self.lon = "19.44995246414342"

	def convert_date2unix(self, std_date):
		dt = [int(d) for d in std_date.split("-")]
		return int(time.mktime(datetime(*dt).timetuple()))

	def convert_unix2date(self, unix_date):
		return datetime.utcfromtimestamp(int(unix_date)).strftime('%Y-%m-%d')

	def get_forecast(self):
		url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
		querystring = {"q": "Lodz,pl", "lat": self.lat, "lon": self.lon, "id": "2172797", "units": "metric", "mode": "JSON", "cnt": 16}
		headers = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com", "X-RapidAPI-Key": self.key}
		req = requests.request("GET", url, headers=headers, params=querystring)
		if req.status_code == 200:
			return json.loads(req.text)
		else:
			raise self.my_exception()

	def get_historical(self, historical_date):
		url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"
		querystring = {"lat": self.lat, "lon": self.lon, "id": "2172797", "units": "metric", "mode": "JSON", "dt": f"{self.convert_date2unix(self.date2check)}"}
		headers = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com", "X-RapidAPI-Key": self.key}
		req = requests.request("GET", url, headers=headers, params=querystring)
		if req.status_code == 200:
			return json.loads(req.text)
		else:
			raise self.my_exception()

	def value_answer_future(self, weather_description):
		if weather_description is None:
			return "Nie wiem"
		elif "rain" in weather_description:
			return "Będzie padać"
		else:
			return "Nie będzie padać"

	def value_answer_past(self, weather_description):
		if weather_description is None:
			return "Nie wiem"
		elif "rain" in weather_description:
			return "Padało"
		else:
			return "Nie padało"

	def prepare_answer(self):
		if self.check_in_file():
			self.load_from_file()
		elif self.today > self.date2check:
			j = w.get_historical(self.date2check)
			self.save_to_file(self.date2check, self.value_answer_past(j["current"]["weather"][0]["description"]))
		else:
			for day in w.get_forecast()["list"]:
				if self.convert_unix2date(day["dt"]) == self.date2check:
					self.save_to_file(self.date2check, self.value_answer_future(day["weather"][0]["description"]))
					return
			self.save_to_file(self.date2check, "Nie wiadomo")

	def save_to_file(self, date, info):
		print(info+"\n")
		with open("records.txt", "a") as file:
			file.write(date + "," + info + "\n")

	def load_from_file(self):
		with open("records.txt", "r") as file:
			for row in file.readlines():
				if self.date2check in row:
					print(row.split(",")[1])

	def check_in_file(self):
		with open("records.txt", "r") as file:
			for row in file.readlines():
				if self.date2check in row:
					return True
			return False

if __name__ == "__main__":
	w = Weather(sys.argv[1:])
	try:
		w.prepare_answer()
	except w.my_exception:
		pass

