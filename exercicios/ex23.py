import pygame #usado para jogos

pygame.init() #inicia o pygame

pygame.mixer.init()

pygame.mixer.music.load() #carrega a musica
pygame.mixer.music.play() #toca a musica
input() #pausa o programa até você apertar Enter dando tempo do pygame inicializar corretamente
pygame.event.wait()