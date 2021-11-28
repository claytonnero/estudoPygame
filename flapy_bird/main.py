import pygame, random
from pygame.locals import *
import itens

width, height = 800, 600
gover = True
cair = False
game = True
asas = 0

pygame.init()
win = pygame.display.set_mode((width, height))

bird0 = pygame.image.load("img/flp0.png")
bird1 = pygame.image.load("img/flp1.png")
piso = pygame.image.load("img/piso.png")
cena = pygame.image.load("img/fundo.png")
tubo = pygame.image.load("img/tubo.png")


#objetos
ply = itens.Itens(win, 200, height/3, 50, 50, bird0, 0)

fundo0 = itens.Itens(win, 0, 210, 0, 0, cena, 0)

fundo1 = itens.Itens(win, width, 210, 0, 0, cena, 0)

def paint():
    global asas
    pygame.display.update()
    pygame.time.delay(10)
    win.fill(0x3C2EE)

    
    
    asas += 1
    if asas >10:
        ply.img = bird0
    else:
     ply.img = bird1
    
    if asas > 20:
        asas = 0
          
    #movendo o cenario
    if fundo0.x < -width:
        fundo.x = 0
        fundo.x = width
        
    fundo0.x -= 1
    fundo1.x -= 1

    fundo0.show()
    fundo1.show()
    ply.show()
    
def control():
    global gover

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            return False

    return True

while game:
    paint()
    game = control()