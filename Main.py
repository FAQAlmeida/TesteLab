from TestesDir import ValidarIdentidade, Sorter, ScreenCapture
from Util import Util as u


class Main:
    options = {1: 'ID',
               2: 'Sorter',
               3: 'screenlog',
               4: 'regular expressions',
               0: 'sair'}

    def __init__(self):
        try:
            self.menu()
            self.switch(input('Digite sua escolha: '))
        except Exception as ex:
            print(ex)

    @classmethod
    def menu(cls):
        try:
            print('\nMenu de Testes', end='\n')
            for key in cls.options.keys():
                print('{0}) {1}'.format(key, cls.options[key].upper()))
        except Exception as ex:
            raise ex

    @classmethod
    def switch(cls, resp: str):
        try:
            if u.equals(resp, '1') or u.equals(resp.upper(), 'ID'):
                ValidarIdentidade.Main()
            elif u.equals(resp, '2') or u.equals(resp.upper(), 'SORTER'):
                Sorter.Main()
            elif u.equals(resp, '3') or u.equals(resp.upper(), 'SCREENLOG'):
                ScreenCapture.ScreenCapture()
            elif u.equals(resp, '4') or u.equals(resp.upper(), 'REGULAR EXPRESSIONS'):
                pass
            elif u.equals(resp, '0') or u.equals(resp.upper(), 'SAIR'):
                exit(0)
        except Exception as ex:
            raise ex


while True:
    Main()
