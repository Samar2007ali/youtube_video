import pygame
pygame.mixer.init()
def play_song():
    name = input("Which song is to be played = ")
    name = name+".mp3"
    pygame.mixer.music.load(name)
    a = input("song ready press enter to play")
    pygame.mixer.music.play()
while True:
    play_song()
