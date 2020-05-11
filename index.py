import requests
from bs4 import BeautifulSoup

# from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# print(soup.find_all('p', class_='outer-text'))
# print(soup.find_all(class_="inner-text" , id="first"))

# print(soup.select('.inner-text p'))

# print(list(soup.children))

# print([type(item) for item in list(soup.children)])


# html = list(soup.children)[2]



# body = list(html)[3]


# p = list(body)[1]

# print("Text is: " + p.get_text() )


# print(soup.find_all('p')[0].get_text())

# print(soup.find('p').get_text())

print(soup.select('div p'))