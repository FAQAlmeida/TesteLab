from Util import Util as u


class Main:
    def __init__(self):
        try:
            options = {1: 'String', 0: 'menu'}
            while True:
                for key in options.keys():
                    print('{0}) {1}'.format(key, options[key].upper()))
                resp = input('Escolha a opção: ')
                if u.equals(resp, '1') or u.equals(resp.upper(), 'STRING'):
                    strsorted = self.strsort(input('Insira a string:\n'))
                    for word in strsorted:
                        print(word, end=' ')
                    print('\n')
                elif u.equals(resp, '0') or u.equals(resp, 'MENU'):
                    break
        except Exception as ex:
            raise ex

    @classmethod
    def strsort(cls, lista: str) -> list:
        try:
            lista = lista.lower().split()
            lista.sort()
            return lista
        except Exception as ex:
            raise ex
