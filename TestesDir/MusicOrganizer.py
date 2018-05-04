import os
import shutil


class Organizer:
    def __init__(self):
        self.path = 'E:\\'
        self.musics = os.listdir(f'{self.path}\\Geral')
        self.cat = {'s': 'SERTANEJO', 'p': 'POP', 'u': 'UNIVERSITARIO', 'e': 'ELETRONICA', 'r': 'RAPPA'}
        self.organizer(self.path)

    def organizer(self, path):
        for music in self.musics:
            dire = input(f'{music}\nDeve ser movido para onde?:\n')
            try:
                shutil.move(f'{self.path}\\Geral\\{music}', f'{self.path}\\{self.cat[dire]}\\{music}')
            except:
                shutil.move(f'{self.path}\\Geral\\{music}', f'{self.path}\\Default\\{music}')


Organizer()
