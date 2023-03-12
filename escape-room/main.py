import textos, funcoes, objetos
from time import sleep

# cria senhas
senha_porta = funcoes.criar_senha()
senha_bau = funcoes.criar_senha()

# printa os textos introdutorios
textos.intro(2.0)
sleep(2.0)

inventario = []
sair = False
cofre = False

while sair == False:

    # mostra as escolhas e printa o cofre caso ele tenha sido descoberto
    escolha = textos.menu(2.0, cofre)
    escolha = escolha.casefold()
    sleep(1.5)

    if escolha == "porta":
        aberta = objetos.porta(senha_porta, sair)
        if aberta == True:
            sair = True

    elif escolha == "janela":
        objetos.janela()

    elif escolha == "mochila":
        objetos.mochila(inventario)

    elif escolha == "vaso":
        objetos.vaso(inventario)

    elif escolha == "gaveta":
        objetos.gaveta(inventario)

    elif escolha == 'quadro':
        objetos.quadro(cofre)
    
    elif escolha == 'bau':
        objetos.bau(inventario, senha_bau)

    elif escolha == "tapete":
        objetos.tapete(senha_bau)

    elif escolha == 'espelho':
        objetos.espelho(inventario, senha_porta)
    
    elif escolha == 'estante':
        pass

    else:
        funcoes.narrador("Você digitou algo errado, tente sem acentos.")

    # mostra inventario e limpa o console
    print(inventario)
    funcoes.limpar()
