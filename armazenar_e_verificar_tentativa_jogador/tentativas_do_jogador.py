from escolha_da_palavra_secreta.escolha_palavra_da_secreta import limpando_string_dos_acentos
# "retirar '_jogo' do inicio"
from fechando_o_jogo.fechando_o_jogo import saindo_do_jogo
# "retirar 'o_jogo' do inicio"


def tentativa_do_usuario():
    while True:
        tentativa = input('''
            Digite a letra que você acha que está na palavra
            Digite [Sair] para fechar o jogo! 
        '''.replace('    ', ''))
        tentativa = limpando_string_dos_acentos(tentativa).upper().strip()
        if tentativa == 'SAIR':
            return saindo_do_jogo()
        if tentativa.isalpha():
            return tentativa
        else:
            print('O jogo aceita somente LETRAS!')


def quantas_letras_tem_na_palavra(palavra_secreta):
    espaco_das_letras = ["_" for letra in palavra_secreta]
    return espaco_das_letras


def marca_tentativa_correta(chute, palavra_secreta, espaco_das_letras):
    for i in range(len(palavra_secreta)):
        if chute == palavra_secreta[i]:
            espaco_das_letras[i] = palavra_secreta[i]
