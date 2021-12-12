import pygame


def ganhou():
    pygame.mixer.init()
    pygame.init()

    pygame.mixer.music.load("E:\\Projeto_Mod_02_backup\\o_jogo\\audios_perdeu_ganhou\\ganhou.mp3")
    # observação para caminho do arquivo que será alterado no download

    pygame.mixer.music.play()
    pygame.event.wait()


def perdeu():
    pygame.mixer.init()

    pygame.init()
    # inicializa
    pygame.mixer.music.load("E:\\Projeto_Mod_02_backup\\o_jogo\\audios_perdeu_ganhou\\perdeu.mp3")
    # carregar o som
    # observação para caminho do arquivo que será alterado no download

    pygame.mixer.music.play()
    # tocar o som
    pygame.event.wait()
    # comando parar o som
