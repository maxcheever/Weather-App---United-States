from bs4 import BeautifulSoup as bs
import requests as r
import datetime as dt

api = 'f37ce4b32816fe61e19784ce5544c1e4'

def wxUnderSoup(city, state):
  City = city.lower()
  State = state.lower()

  if ' ' in City:
    City.replace(' ', '-')

  url = f'https://www.wunderground.com/weather/us/{State}/{City}'
  response = r.get(url)
  page = response.text
  soup = bs(page, 'html.parser')

  return soup

def getCoords(city, state):
  soup = wxUnderSoup(city, state)
  coords = soup.find_all('strong')
  lat = coords[1].text
  lon = str(-1*float(coords[2].text))

  return lat, lon

def weather(lat, lon, apiKey):
  part = 'minutely, hourly'
  url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={apiKey}&units=imperial'
  response = r.get(url)
  wxJson = response.json()
  
  return wxJson

def getForecast(city, state):
  cityLat, cityLon = getCoords(city, state)
  wxFC = {'day':[], 'hi':[], 'lo':[], 'wxDescr':[]}

  for index in range(1, 5):
    wxJson = weather(cityLat, cityLon, api)
    unixDate = wxJson['daily'][index]['dt']
    weekday = dt.datetime.fromtimestamp(unixDate).strftime('%a')

    hi = wxJson['daily'][index]['temp']['max']
    lo = wxJson['daily'][index]['temp']['min']
    cond = wxJson['daily'][index]['weather'][0]['main']

    wxFC['day'].append(weekday)
    wxFC['hi'].append(hi)
    wxFC['lo'].append(lo)
    wxFC['wxDescr'].append(cond)

  return wxFC

def getCurrentWX(city, state):
  soup = wxUnderSoup(city, state)
  current = soup.find(class_='wu-value wu-value-to').text
  feels = soup.find(class_='temp').text
  dateTime = soup.find(class_='timestamp').span.strong.text
  windSpd = soup.find(class_='wind-speed').strong.text
  condition = soup.find(class_="condition-icon small-6 medium-12 columns").text
  humidity = soup.find(class_="test-false wu-unit wu-unit-humidity ng-star-inserted").span.text
  hi = soup.find(class_="hi").text
  lo = soup.find(class_="lo").text

  currentDictWX = {'current': current, 'feels': feels, 'dateTime': dateTime, 'windSpd': windSpd, 'condition': condition, 'humidity': humidity, 'hi': hi, 'lo': lo}
  
  return currentDictWX