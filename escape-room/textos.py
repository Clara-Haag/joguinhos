from time import sleep
def intro(tempo):
    print('Narrador: Você acorda em uma sala misteriosa...')
    sleep(tempo)
    print('Você: Como que cheguei aqui?')
    sleep(tempo)
    print('Narrador: Você olha ao redor e vê que pode fuçar em algumas coisas')

def menu(tempo, cofre):
    print('Objetos da sala\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    sleep(tempo)
    print('- Porta\n- Janela\n- Mochila\n- Vaso\n- Gaveta\n- Quadro\n- Baú\n- Tapete\n- Espelho\n- Estante')
    if cofre == True:
        print('- Cofre')
    escolha = str(input('Onde você vai procurar? '))
    return escolha