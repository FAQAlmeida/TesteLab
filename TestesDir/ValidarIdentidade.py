from Util import Util as u


class Main:
    def __init__(self):
        try:
            options = {1: 'CPF', 2: 'CNPJ', 0: 'menu'}
            while True:
                for key in options.keys():
                    print('{0}) {1}'.format(key, options[key].upper()))
                resp = input('Digite a sua escolha: ')
                if u.equals(resp, '1') or u.equals(resp.upper(), 'CPF'):
                    print(Cpf().is_cpf(input('Digite o cpf: ')))
                elif u.equals(resp, '2') or u.equals(resp.upper(), 'CNPJ'):
                    print(Cnpj().is_cnpj(input('Digite o cnpj: ')))
                elif u.equals(resp, '0') or u.equals(resp.upper(), 'MENU'):
                    break
        except Exception as ex:
            raise ex


class Cpf:
    chars = ['.', '/', '-']

    @classmethod
    def is_cpf(cls, cpf: str):
        try:
            dgs = [10, 9, 8, 7, 6, 5, 4, 3, 2]
            r = 0
            for x in range(len(cpf) - 2):
                if cpf[x] not in cls.chars:
                    r += (int(cpf[x]) * dgs.pop(0))
            r %= 11
            if r >= 2:
                ver = 11 - r
            else:
                ver = 0
            if u.equals(ver, cpf[len(cpf) - 2]):
                dgs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
                r = 0
                for x in range(len(cpf) - 1):
                    if cpf[x] not in cls.chars:
                        r += (int(cpf[x]) * dgs.pop(0))
                r %= 11
                if r >= 2:
                    ver = 11 - r
                else:
                    ver = 0
                if u.equals(ver, cpf[len(cpf) - 1]):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as ex:
            raise ex


class Cnpj:
    chars = ['.', '/', '-']

    def is_cnpj(self, cnpj: str):
        try:
            dgs = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            r = 0
            for x in range(len(cnpj) - 2):
                if cnpj[x] not in self.chars:
                    r += (int(cnpj[x]) * dgs.pop(0))
            r %= 11
            if r >= 2:
                ver = 11 - r
            else:
                ver = 0
            if str(ver).__eq__(cnpj[len(cnpj) - 2]):
                dgs = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                r = 0
                for x in range(len(cnpj) - 1):
                    if cnpj[x] not in self.chars:
                        r += (int(cnpj[x]) * dgs.pop(0))
                r %= 11
                if r >= 2:
                    ver = 11 - r
                else:
                    ver = 0
                if str(ver).__eq__(cnpj[len(cnpj) - 1]):
                    return True
                else:
                    return False
            else:
                return False
        except TypeError as ex:
            raise ex.__new__(Cnpj)
        except Exception as ex:
            raise ex
