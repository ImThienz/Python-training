"Menu Pygame"
from mimetypes import inited

# import pygame, sys
# from pygame.locals import *
#
# pygame.init()
#
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
#
# while True:
#     for even in pygame.event.get():
#         if even.type == QUIT:
#             pygame.quit()
#             sys.quit()
#
#     DISPLAYSURF.fill((255, 255, 255))
#     pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (100, 80, 150, 50))
#     pygame.display.update()


""
import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Bit Racey')

black=(0,0,0)
white=(255,255,255)

clock=pygame.time.Clock()
crashed=False
carImg=pygame.image.load('racecar.jpg')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x=(display_width*0.45)
y=(display_height*0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True
    gameDisplay.fill(white)
    car(x,y)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()