import requests
from bs4 import BeautifulSoup



def print_ip(responce):
    try:
        soup = BeautifulSoup(responce.text, 'html.parser').find('div', class_='ip-info_left').find('div', class_='ip-info').find('div', class_='ip')
        return print(soup.text.strip())
    except:
        return None
