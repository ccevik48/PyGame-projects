import pygame
import random
pygame.init()

width = 600
height = 500


window = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")

x = width//2
y = height//2
score = 0
snake = [(x,y)]
direction = 'R'
apple = [random.randrange(0,width,10),random.randrange(0,height,10)]

def spawnApple():
    apple[0],apple[1] = random.randrange(0,width,10),random.randrange(0,height,10)

def reset():
    global x
    global y
    global direction
    global snake
    x = width//2
    y = height//2
    direction = 'R'
    snake = [(x,y)]
    apple[0],apple[1] = random.randrange(0,width,10),random.randrange(0,height,10)



run = True
while run:

    pygame.time.delay(125)
    # print(score)
    window.fill((0,0,180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #if eat food
    if x == apple[0] and y == apple[1]:
        score += 1
        snake.append((x,y))
        spawnApple()


    # detect direction change
    if keys[pygame.K_RIGHT] and direction != 'L':
        direction = 'R'
    if keys[pygame.K_LEFT] and direction != 'R':
        direction = 'L'
    if keys[pygame.K_UP] and direction != 'D':
        direction = 'U'
    if keys[pygame.K_DOWN] and direction != 'U':
        direction = 'D'

    # change direction
    if direction == 'R':
        x+=10
    if direction == 'L':
        x-=10
    if direction == 'U':
        y-=10
    if direction == 'D':
        y+=10

    #draw snake
    del snake[-1]
    snake.insert(0,(x,y))
    for s in snake:
        pygame.draw.rect(window, (0,255,0), (s[0],s[1],10,10))
    
    # detect collision
    if x < 0 or x > width or y < 0 or y > height:
        reset()

    #if ate self
    if len(snake) != len(set(snake)):
        reset()


    # draw things
    pygame.draw.rect(window, (255,0,0), (apple[0],apple[1],10,10))
    pygame.draw.rect(window, (0,155,0), (x,y,10,10))
    
    pygame.display.update()



pygame.quit()