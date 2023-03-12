from time import sleep
import funcoes


def porta(senha, aberta):
    abrir = input("Digite a senha: ")
    if abrir == senha:
        aberta = True
        funcoes.narrador("Parabéns! Você saiu da sala misteriosa!", True)
        return aberta
    else:
        funcoes.narrador("Senha incorreta, tente novamente.")


def janela():
    funcoes.narrador("Da janela dá pra ver uma tempestade de neve, não dá para ver nada...", True)
    funcoes.narrador("'Preciso me esquentar, acho que tenho algo na mochila.'")


def mochila(inv):
    funcoes.narrador("'Meu casaco!'")
    inv.append("Casaco")
    return inv


def vaso(inv):
    funcoes.narrador("Você encontrou uma chave.", True)
    inv.append("chave_gaveta")
    return inv


def gaveta(inv):
    tempo = 1.5
    if "chave_gaveta" in inv:
        funcoes.narrador('Há um diário dentro da gaveta', True)
        sleep(tempo)
        escolha = input('Desejas lê-lo? s/n\n')
        if escolha == 's':
            sleep(tempo)
            funcoes.narrador("Meu diário <3\n=-=-=-=-=-=-=-=-=-=-=")
            sleep(tempo*2)
            funcoes.narrador("DIA 01:Hoje acordei em uma maca, um médico me disse que sofri um acidente de carro e acabei tendo amnésia... O quê explica esse povo estranho falando que sou parente deles")
            sleep(tempo*2)
            funcoes.narrador("DIA 02: Eu não sei onde estou, eu abri essa gaveta e vi este diário. Acho que não amnésia e sim alzheimer...")
            sleep(tempo*2)
            funcoes.narrador('O resto do caderno está em branco', True)
    else:
        funcoes.narrador('A gaveta está trancada...')


def quadro(cofre: bool):
    funcoes.narrador("Você percebe que há algo de estranho no quadro... Talvez se...", True)
    funcoes.narrador("Há um cofre atrás dele!", True)
    cofre = True
    return cofre


def bau(inv, senha):
    combinacao = input("Coloque a combinação: ")
    if combinacao == senha:
        funcoes.narrador("Você abre o baú e acha uma chave!", True)
        inv.append("chave_estante")
        return inv
    else:
        funcoes.narrador("Senha incorreta.")


def tapete(senha):
    funcoes.narrador(f"Você mexe um pouco o tapete e vê um papel: {senha}")


def espelho(inv, senha):
    if 'marreta' in inv:
        funcoes.narrador("'MARRETADAAAA!!!'")
        funcoes.narrador(f"Você acha um papel que estava dentro dele: {senha}", True)
    else:
        funcoes.narrador("'Olha eu! Eu odeio espelhos, que vontade de marretar ele...")


def estante(inv):
    if "chave_estante" in inv:
        funcoes.narrador("Ao mexer em alguns livros você encontra uma chave!", True)
        inv.append("chave_cofre")
        return inv


def cofre(inv):
    if "chave_cofre" in inv:
        funcoes.narrador("'Olha uma marreta!'")
        inv.append("marreta")
        return inv
    else:
        funcoes.narrador("Você precisa de uma chave para abri-lo...", True)

if __name__ == "__main__":

    janela()