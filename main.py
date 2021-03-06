import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display = pygame.Surface((240, 160))

grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0,0,0))

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (0 + x * 16 - y * 16, 0 + x * 8 + y * 8))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(1)