import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XrmcEHUzbeQ')

soup = BeautifulSoup(page.content, 'html.parser')


forecast_container = soup.select('li.forecast-tombstone')

periods = [ item.find('p').get_text() for item in forecast_container]
print(periods)

temps = [ item.select('p.temp')[0].get_text() for item in forecast_container]
print(temps)


img_elements = [ item.find('img') for item in forecast_container]
weather_descriptions = [ item['alt'] for item in img_elements]

print(weather_descriptions)



