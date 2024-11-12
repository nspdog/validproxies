import parse_table
import requests
from cfg import headers

#функция отбора валидных проксей
def checking_values(parsed_proxie_list):
    value_proxie_list = []
    responce = requests.get('https://2ip.ru/', headers=headers)
    if responce.status_code == 200:
        value_proxie_list.append

if __name__ == '__main__':
    checking_values(parse_table.parse())
