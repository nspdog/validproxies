

class Proxie():
    def __init__(self, ip, port, https, anon = None):
        self.ip = ip
        self.port = port
        self.https = https
        self.anon = anon





    #возвращает булевое значение; 1 = используется https, 0 =  используется http
    #wh = which hhtp

    #возвращает строку айпи:порт
    def do(self):
        if self.https =='yes':
            self.https = 'https'
        else:
            self.https = 'http'
    
    #элемент с http убираем и делаем проверку уже в процессе отправки запроса
        return {'http' : f"{self.https}://{self.ip}:{self.port}",
                'https' : f"{self.https}://{self.ip}:{self.port}"}
    
class Resp():
    def __init__(self, resp, status_code):
        self.resp = resp
        self.status_code = status_code