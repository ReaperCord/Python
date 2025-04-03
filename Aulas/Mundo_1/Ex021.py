#Crieum script que busque e reproduza um arquivo de audio mp3
import os.path

import pygame

audioPath = os.path.join("mp3", "KIT SALVE DA QUEBRADA- Versão anos 50 🍷.mp3")

pygame.init()
pygame.mixer.music.load(audioPath)
pygame.mixer.music.play()

input("Pressione qualquer tecla para sair...")
pygame.mixer.quit()
