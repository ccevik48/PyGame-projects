import pygame
from datetime import datetime
import time
import math



pygame.init()

width = 400
height = 300

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Time")
# icon = pygame.image.load('clock.png')
# pygame.display.set_icon(icon)
pygame.font.init() 


run = True
while run:
    pygame.time.delay(100)

    now = datetime.now()
    unixTime = math.floor(time.time())
    currentTime = now.strftime("%d/%m/%Y")
    currentTime2 = now.strftime("%H:%M:%S")
    myfont = pygame.font.SysFont('Helvetica', 72)
    textsurface = myfont.render(currentTime, False, (0, 220, 0))
    textRect = textsurface.get_rect()
    textRect.center = (width // 2, 3 * height // 10)
    textsurface2 = myfont.render(currentTime2, False, (0, 220, 0))
    textRect2 = textsurface2.get_rect()
    textRect2.center = (width // 2, 7 * height // 10)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    window.fill((10,10,10))

    window.blit(textsurface,textRect)
    window.blit(textsurface2,textRect2)
    
    pygame.display.update()

