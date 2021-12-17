from escolha_da_palavra_secreta.escolha_palavra_da_secreta import *
from multiplayer_do_jogo.multiplayer import *
from verificar_se_o_jogador_acertou_ou_errou.verificar_jogador_acertou_errou import *


palavras = carregar_palavras_texto('escolha_das_palavras/paises.txt')
jogadores = quantos_jogadores()


def play(palavras, jogadores):
    separador_de_linhas = enfeite()
    quantidade_de_palavras = len(palavras)
    while quantidade_de_palavras > 0:
        status = True
        for nome, valor in jogadores.items():
            if quantidade_de_palavras == 0:
                continue
            if len(jogadores[nome]['status']) == 0:
                palavra = palavra_selecionado(palavras)
                jogadores[nome]['palavras'].append(palavra)
                jogadores[nome]['tentativas'].append(list())
                quantidade_de_palavras -= 1
            print(f'''
                Usuário: {nome}
                Letras erradas até agora: {jogadores[nome]["tentativas"]}, 
                {nome} ganhou {jogadores[nome]['ganhou']} 
                {nome}` perdeu {jogadores[nome]['perdeu']}
            '''.replace('    ', ''))
            print(separador_de_linhas)
            jogador_acertou_ou_errou(jogadores, nome)


play(palavras, jogadores)
