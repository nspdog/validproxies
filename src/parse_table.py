import requests
import lxml
import time
from cfg import headers, url, check_url
from bs4 import BeautifulSoup
from utils import Proxie
from parse2ip import print_ip
from threading import Thread

def main():    
    own_timer = time.time()
    parsed_proxie_list = []
    valid_proxies = []
    anon_proxies = []
    parse(parsed_proxie_list)
    print('successefully parsed')
    
    
    thread_counter = 0
    for i in range(300):
        thread = Thread(target = find_valid, args=((parsed_proxie_list[i].do(), valid_proxies)))
        thread.start()
        print('new thread was started: ', i)
        if i == 299:
            thread.join()
            return [valid_proxies, anon_proxies]   
         

def get_req(url, headers, proxy = None, valid_proxies = None):
    get_req_status = 0
    #проверяем есть ли необязательный параметр прокси
    #выполняем запрос исходя из условий
    
    if proxy != None:
        try:
            responce = requests.get(url=url, headers=headers, proxies=proxy)
            print(proxy, '  success')
            print_ip(responce, '\n')
            valid_proxies.append(proxy)
        
        except:
            pass
            #print(proxy,  'unsuccess')        
    else:
        responce = requests.get(url=url, headers=headers)
    
        if responce.status_code == 200:
        #print(proxy, ' : success')
            get_req_status_code = 1
            return responce
        
    return get_req_status_code

def find_valid(proxies, valid_proxies):
    find_valid_status_code = 0
    try:
        responce = get_req(check_url, headers = headers, proxy = proxies)
        
        if responce != 0:
            
            find_valid_status_code = 1
            
    except:
        pass    
    return find_valid_status_code
    
#функция парсинга таблички с сайта
def parse(parsed_proxie_list):
    parse_status_code = 1
    
    responce = get_req(url=url, headers=headers)
    
    if (responce!=None):
        #супчик = таблица с проксями; массив данных типа супчика со всеми элементаи таблички
        soup = BeautifulSoup(responce.text, 'html.parser').find("table", class_="table table-striped table-bordered").find("tbody").find_all("tr")
        
        for unsorted_proxie_list_element in soup:
            counter = 0
            
            #вспомогательная переменная, чтобы не ебать мозги, заодно обнуляем ее каждый шаг цикла
            proxy = Proxie(None, None, None)

            #ну я маму ебал делать все через иф элсы, но похуй, по другому никак
            for element in unsorted_proxie_list_element:
                if counter == 6: #https 'yes' or 'no'
                    if element.text.strip() == 'yes':
                        proxy.https = 'https'
                    else:
                        proxy.https = 'http'
                if counter == 0: #айпишник
                    proxy.ip = element.text
                if counter == 1: #порт
                    proxy.port = element.text
                
                
                counter+=1
            
            parsed_proxie_list.append(proxy)
        
        
        
    else:
        print("responce == None")
        parse_status_code = 0
    return parse_status_code

if __name__ == '__main__':
    
    nsp_time = time.time()

    
    #функция мэйн возвращает массив из двух элементов и становится соответствующей переменной
    main = main()
    nsp_proxies = main[0]       # 0 = список прокси
    nsp_anon_proxie = main[1]   # 1 = список анонимных прокси
    
    nsp_time = time.time() - nsp_time
    local_time = time.localtime(nsp_time)
    formatted_time = time.strftime("%M:%S:", local_time)
    print('\nProgramm finished!\nTotal count of valid proxies: ', len(main[0]), '\nTotal time: ', formatted_time)

