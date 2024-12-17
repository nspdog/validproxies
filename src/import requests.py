import requests
from bs4 import BeautifulSoup
from utils import Proxy

def main():
    
    
    responce = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(responce.text, 'html.parser').find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
    proxy = Proxy()
    c = 0
    for soup_line in soup:
        c+=1
        formatted_soup_line = soup_line.find_all('td')
        proxy.set_ip(formatted_soup_line[0].text)
        proxy.set_port(formatted_soup_line[1].text)
        proxy.set_https(formatted_soup_line[6].text.strip())
        proxy.set_country(formatted_soup_line[3].text)
        
        if (formatted_soup_line[4].text != 'transparent'):            
            proxy.set_anon(True)
        else:
            proxy.set_anon(False)
        print(proxy.get_anon())
main()