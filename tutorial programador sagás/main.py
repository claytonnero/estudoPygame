import pygame, random
from pygame.locals import *

def grade_pos():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Cobrinha")

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_pele = pygame.Surface((10, 10))
cobra_pele.fill((255, 255, 255))

pos_maçã = (grade_pos())

maçã = pygame.Surface((10, 10))
maçã.fill((255, 0, 0))

direção = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direção = UP
            if event.key == K_DOWN:
                direção = DOWN
            if event.key == K_LEFT:
                direção = LEFT
            if event.key == K_RIGHT:
                direção = RIGHT
    if colisao(cobra[0], pos_maçã):
        pos_maçã = grade_pos()
        cobra.append((0,0))

    if direção == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)   
    if direção == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)    
    if direção == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])    
    if direção == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    for i in range(len(cobra) -1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    tela.fill((0, 0, 0))
    tela.blit(maçã, pos_maçã)
    
    for pos in cobra:
        tela.blit(cobra_pele, pos)
    
    pygame.display.update()
