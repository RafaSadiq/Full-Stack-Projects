import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_g(links):
    titles = []

    def post(url):
        if 'winter' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
            if link.get('href') == None:
                continue
            else:
                post(link.get("href"))
            post(link['href'])

    return titles


r = requests.get('https://www.cnn.com')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_g(links)

for title in titles:
    print(title)

print(title_g(links))