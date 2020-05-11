import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XrmcEHUzbeQ')

soup = BeautifulSoup(page.content, 'html.parser')


