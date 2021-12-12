from o_jogo.fechando_o_jogo.fechando_o_jogo import *
from o_jogo.enfeite_e_desenhos.enfeites_e_arte import enfeite


def leia_int():
    separador_de_linha = enfeite()
    while True:
        mensagem = input('''Qual a sua escolha jogador 
        1 - Para um jogador
        2 - Para dois jogadores
        3 - Para três jogadores
        4 - Para quatro jogadores
        Digite [Sair] para fechar o jogo
    '''.replace('    ', '')).upper().strip()
        print(separador_de_linha)
        if mensagem == 'SAIR':
            saindo_do_jogo()
        if mensagem.isnumeric():
            num_jogadores = mensagem
            num_jogadores = int(num_jogadores)
            if num_jogadores <= 4 and num_jogadores != 0:
                return num_jogadores
        else:
            print('Digite um comando válido!')
            print(separador_de_linha)


def nome_jogadores():
    separador_de_linha = enfeite()
    while True:
        nome_jogador = input('Digite um nome: ').capitalize().strip()
        if nome_jogador == 'Sair':
            saindo_do_jogo()
        if nome_jogador.isalpha():
            print(separador_de_linha)
            return nome_jogador
        else:
            print(separador_de_linha)
            print(f'''
                Um dos nomes contém caracteres proibidos. 
                Aceitamos somente caracteres alfabéticos!
                Resetando!
            '''.replace('    ', ''))
            print(separador_de_linha)
            sleep(1.5)


def quantos_jogadores():
    jogadores = {}

    numero_de_jogadores = leia_int()
    for x in range(numero_de_jogadores):
        nome_jogador = nome_jogadores()
        jogadores[nome_jogador] = dict(
            {
                'palavras': list(),
                'tentativas': list(),
                'status': list(),
                'ganhou': 0,
                'perdeu': 0
            }
        )
    return jogadores