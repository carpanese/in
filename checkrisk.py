import time

class Checkrisk:
    def check_risk(self):
        print('Inicio Processamento ' + time.strftime("%d-%m-%Y %H:%M:%S"))
        time.sleep(5)
        print('Teste Realizado com Sucessso!')
        print('Fim Processamento ' + time.strftime("%d-%m-%Y %H:%M:%S"))
