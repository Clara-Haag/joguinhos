import os, random

from time import sleep
from sys import stdout as s


def limpar():
    continuar = input('Aperte ENTER para continuar')
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_senha():
    senha1 = str(random.randint(0,9))
    senha2 = str(random.randint(0,9))
    senha3 = str(random.randint(0,9))
    senha = senha1+senha2+senha3
    return senha

def narrador(texto: str, narrador: bool = False):
    if narrador == True:
        s.write("Narrador: ")
    for letra in texto:
        s.write(letra)
        sleep(0.1)
    s.write("\n")

if __name__ == "__main__":

    narrador("teste amores...", True)
