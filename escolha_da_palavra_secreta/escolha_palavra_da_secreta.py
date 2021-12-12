import unicodedata
from random import randrange


def carregar_palavras_texto(nome_arquivo="file.txt"):
    with open(nome_arquivo, encoding='utf8') as arquivo:
        palavras = list(arquivo.read().splitlines())

    return palavras


def limpando_string_dos_acentos(string):
    return ''.join(letra for letra in unicodedata.normalize('NFD', string)
                   if unicodedata.category(letra) != 'Mn')


def palavra_selecionado(palavras):
    if len(palavras) == 1:
        palavra_secreta = palavras[0]
        palavras.remove(palavra_secreta)
        palavra_secreta = limpando_string_dos_acentos(palavra_secreta)
        return palavra_secreta.upper().strip()

    palavra_aleatoria = randrange(0, len(palavras) - 1)
    palavra_secreta = palavras[palavra_aleatoria]
    palavras.remove(palavra_secreta)
    palavra_secreta = limpando_string_dos_acentos(palavra_secreta)
    return palavra_secreta.upper().strip()