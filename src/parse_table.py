import requests
import asyncio
import lxml
import time
from cfg import *
from bs4 import BeautifulSoup
from utils import Proxy
from parse2ip import print_ip
from threading import Thread



async def main():

    valid_proxies = []
    parsed_proxies = parse_table_free_proxy_list()
    tasks = [find_valid(proxy, valid_proxies) for proxy in parsed_proxies]
    await asyncio.gather(*tasks)
    

#функция оправки запроса, возвращает запрос. Универсально работает для всех сайтов в рамках программы
#если в качестве аргумента указывается прокси, функция проверяет его и заносит в массив valid_proxies      

def get_req(url, proxy = None, valid_proxies = None):    
    #проверяем есть ли необязательный параметр прокси
    #выполняем запрос исходя из условий
    
    if proxy is not None:
        response = requests.get(url=url, headers=headers, proxies=proxy)
        
        valid_proxies.append(proxy)
    
    else:
        response = requests.get(url=url, headers=headers)
        
    return response

async def find_valid(proxy, valid_proxies):

    proxies = proxy.do()
    
    try:
        response = get_req(check_url, proxy = proxies)
        response.raise_for_status()  # Проверка на наличие ошибок HTTP
        print_ip(response)
        response.text
        
    except requests.exceptions.RequestException as e:
        None   
        
    
    

    
#функция парсинга таблички с сайта
def parse_table_free_proxy_list():
    parsed_proxy_list = []
    
    response = get_req(url=url_free_proxy_list_net)
    
    if (response!=None):
        
        #суп = таблица с проксями; массив данных типа суп со всеми элементами таблицы
        response = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(response.text, 'html.parser').find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
        
        
        for soup_line in soup:
            proxy = Proxy()
            formatted_soup_line = soup_line.find_all('td')
            proxy.set_ip(formatted_soup_line[0].text)
            proxy.set_port(formatted_soup_line[1].text)
            proxy.set_https(formatted_soup_line[6].text.strip())
            proxy.set_country(formatted_soup_line[3].text)
            
            if (formatted_soup_line[4].text != 'transparent'):            
                proxy.set_anon(True)
            else:
                proxy.set_anon(False)
            parsed_proxy_list.append(proxy)
    else:
        print('Failed response table')   
            
    return parsed_proxy_list


#допилить парсинг на селениуме
def parse_table_freeproxy_cz():
    
    parsed_proxy_list = []
    response = get_req(url = url_free_proxy_cz)
    if response != None and response.status_code == 200:
        pass
    
#допилить парсинг на селениуме    
def parse_gologin():
    
    parsed_proxy_list = []
    response = get_req(url=url_gologin)
    
    if (response != None and response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.find('tbody', class_='fp-body'))
        
        
    return None
        
def parse_proxy_sale():
    
    parsed_proxy_list = []
    response = get_req(url=f'{url_proxy_sale}1')
    
    if (response != None and response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser').find()
        print(soup.find('div', class_ = 'proxy__table'))
        
        
    return None
        
        
        



if __name__ == '__main__':
    parse_gologin()
    #asyncio.run(main())

