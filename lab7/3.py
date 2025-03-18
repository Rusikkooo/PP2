import pygame
import sys
import os

pygame.init() 
HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Ruslan`s display")

bg_color = (255,255,255)
circle_color = (255,0,0)
border_color = (0,0,0) # шегара түсі

running = True

circle_x = 30
circle_y = 30 
circle_radius = 25 #фигура колемы

clock = pygame.time.Clock()#частота кадров
while running:
    
    for event in pygame.event.get():
        print(event)  
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill(bg_color)    
    
    pressed  = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:circle_y-=20
    if pressed[pygame.K_DOWN]:circle_y+=20
    if pressed[pygame.K_LEFT]:circle_x-=20
    if pressed[pygame.K_RIGHT]:circle_x+=20
    
    circle_y = max(circle_radius,min(HEIGHT - circle_radius,circle_y))
    circle_x = max(circle_radius,min(WIDTH - circle_radius,circle_x))
    
        
    pygame.draw.circle(screen, circle_color,(circle_x,circle_y),circle_radius)
    pygame.draw.circle(screen,border_color,(circle_x,circle_y),circle_radius,3) #шаршы шегарасы
    clock.tick(120)
    pygame.display.flip()
    
pygame.quit()
sys.exit()
