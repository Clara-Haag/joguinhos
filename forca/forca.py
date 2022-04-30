from random import choice
from sys import stdout as s
import homi

def imprimir(frase):
    for i in frase:
        s.write(f'{i} ')

# (key) palavra : (value) dica
respostas = homi.respostas
pergunta, dica = choice(list(respostas.items()))
palavra = []
resposta = []

for i in pergunta:
    palavra.append(i)
for i in range(len(palavra)):
    resposta.append('-')

erros = 0
acertos = 0
ajuda = False

while erros < 6 and acertos != len(palavra):

    if ajuda == False:
        print("Dica: digite 'dica' para mostrar uma dica!")
    else:
        print(f'Dica: {dica}')
    
    letra = input('Qual é o seu palpite? ')

    if letra == 'dica':
        ajuda = True
    else:
        if letra not in palavra: # se a letra não existe
            erros += 1
        else: # caso sim
            for i in palavra:
                if letra == i:
                    indice = palavra.index(i)
                    resposta[indice] = letra
                    palavra[indice] = '-' # remove a letra da palavra, evitando problemas com letras repetidas!
                    acertos += 1

    homi.forca(erros)
    imprimir(resposta)
    print(f'\nAcertos: {acertos} | Erros: {erros}')
    
if acertos == len(palavra):
    print('Parabéns você ganhou!')
else:
    homi.morte()
    print('Você morreu...')
