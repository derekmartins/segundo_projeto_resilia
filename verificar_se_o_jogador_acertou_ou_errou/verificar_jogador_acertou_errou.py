from armazenar_e_verificar_tentativa_jogador.tentativas_do_jogador import *
from enfeite_e_desenhos.enfeites_e_arte import *

def jogador_acertou_ou_errou(jogadores, nome_jogador):
    separador_de_linha = enfeite()
    palavra = jogadores[nome_jogador]['palavras'][-1]
    enforcou = False
    acertou = False
    erros = 0

    if len(jogadores[nome_jogador]['status']) == 0:
        jogadores[nome_jogador]['status'] = quantas_letras_tem_na_palavra(palavra)

    while not acertou and not enforcou:

        print(f'''
        A palavra tem {len(jogadores[nome_jogador]["status"])} letras
        {jogadores[nome_jogador]["status"]}
        '''.replace('    ',''))

        resposta = tentativa_do_usuario()
        jogadores[nome_jogador]['tentativas'][-1].append(resposta)

        if resposta in palavra:
            marca_tentativa_correta(resposta, palavra, jogadores[nome_jogador]["status"])
            if jogadores[nome_jogador]['status'] == list(palavra):
                print(f' Você ganhou\nA Palavra secreta era: {palavra}')
                jogadores[nome_jogador]['status'] = list()
                jogadores[nome_jogador]['ganhou'] += 1
                print('Você ganhou parabéns!!!!!!!')
                return

        else:
            for x in jogadores[nome_jogador]['tentativas'][-1]:
                if x not in palavra:
                    erros += 1
                    desenha_forca(erros)
                    print(separador_de_linha)
                    if erros == 7:
                        jogadores[nome_jogador]['status'] = list()
                        jogadores[nome_jogador]['perdeu'] += 1
                        print(f'Você ENFORCOU\nA Palavra secreta era: {palavra}')
            return
