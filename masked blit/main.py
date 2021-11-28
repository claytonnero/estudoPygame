import pygame
import personagem
from pygame.locals import *

pygame.init()

w = 1152 
h = 648

dir = 0
mov = 0 

win = pygame.display.set_mode((w, h))
game = True

pos = [[0, 73], [225, 297], [144, 368]]

itens = pygame.image.load("sprite.png")
fundo = pygame.image.load("images.jpeg")
fundo2 = pygame.image.load("indice.jpeg")

frisk = personagem.Personagem(1, 1, 80, 500, 72, 117)

relogio = pygame.time.Clock()

def masked_blit(win, img, wx, wy, x, y, w, h):
    surf = pygame.Surface((w, h)).convert()
    surf.blit(img, (0,0), (wx, wy, w, h))
    alpha = surf.get_at((0, 0))
    surf.set_colorkey(alpha)
    win.blit(surf, (x, y))

def control(obj):
        global dir, mov
        key = pygame.key.get_pressed()
        if key[K_s]:
            obj.x -= 2
            mov -= 1
            dir = 0
        if key[K_f] and obj.x < w - obj.w:
            obj.x += 2
            dir = 1
            mov += 1
        if key[K_UP]:
            dir = 2
            mov = 10
        if key[K_DOWN]:
            dir = 2
            mov = 0

        if mov > 19:
            mov = 0
        if mov < 0:
            mov = 19


while game:

    win.blit(fundo2, (0, 0))

    control(frisk)
    masked_blit(win,itens, pos[dir][int(mov/10)], frisk.wy, frisk.x, frisk.y, frisk.w, frisk.h)
    
    pygame.display.flip()
    win.fill((255, 255, 255))
    
    #relogio.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
