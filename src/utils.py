
class Proxy:
    def __init__(self, ip = None, port = None, https = None, anon = None, country = None):
        self.__ip = ip
        self.__port = port
        self.__https = https
        self.__anon = anon
        self.__country = country
        
    def set_ip(self, ip):
        self.__ip = ip
    
    def set_port(self, port):
        self.__port = port
    
    def set_https(self, https):
        if (https == 'yes'):
            self.__https = 'https'
        else:
            self.__https = 'http'
    
    def set_anon(self, anon):
        self.__anon = anon
        
    def set_country(self, country):
        self.__country = country.lower()

    def get_ip(self):
        return self.__ip
    
    def get_port(self):
        return self.__port
    
    def get_https(self):
        return self.__https
    
    def get_anon(self):
        return self.__anon
    



    #возвращает булевое значение; 1 = используется https, 0 =  используется http
    #wh = which hhtp

    #возвращает строку айпи:порт
    def do(self):    
    #элемент с http убираем и делаем проверку уже в процессе отправки запроса
        return {'http' : f"{self.__https}://{self.__ip}:{self.__port}",
                'https' : f"{self.__https}://{self.__ip}:{self.__port}"}
    
class Resp():
    def __init__(self, resp, status_code):
        self.resp = resp
        self.status_code = status_code