import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-bentley/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5 Safari/537.36' ,
 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'} 

def get_html(url , params=None):
    r = requests.get(url , headers=HEADERS , params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html , 'html.parser')
    items = soup.find_all('a' , class_='proposition_link')
    
    cars = []
    for item in items:
        cars.append({
            'titel':item.find('h3' , class_ = 'proposition_name').get_text(strip=True),
            'price': item.find('span' , class_= 'green bold size22 tooltip-price'),
        })
    print(cars)
    

def parse():
     html = get_html(URL)
     if html.status_code == 200:
         get_content(html.text)


parse()

    