import pygame
import sys
import os
import time 


pygame.init()
H = 800
W = 600
screen = pygame.display.set_mode((H,W))
pygame.display.set_caption("Mickey clock")

Body_image = pygame.image.load("lab7/imagess/mickey.jpeg")
R_hand = pygame.image.load("lab7/imagess/R_hand.png")
L_hand = pygame.image.load("lab7/imagess/L_hand.png")

Body_image = pygame.transform.scale(Body_image,(H,W))
# Center_R = R_hand.get_rect(center=(H//2,W//2))
# Center_L = L_hand.get_rect(center=(H//2,W//2))

clock_center = (H// 2, W // 2)

running = True 
bg_color = (0,0,0)

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running  = False
            
    current_time = time.localtime()
    secunds = current_time.tm_sec 
    minutes = current_time.tm_min
    
    angle_secundes = -secunds * 6
    angle_minutes = -(minutes * 6 + secunds/60 * 6)
    
    Rotated_R_h = pygame.transform.rotate(R_hand, angle_minutes)
    Rotated_L_h = pygame.transform.rotate(L_hand, angle_secundes)
    
    R_hand_rotated_rect = Rotated_R_h.get_rect(center=clock_center)
    L_hand_rotated_rect = Rotated_L_h.get_rect(center=clock_center)
    
    
    screen.fill(bg_color)
    screen.blit(Body_image,(0,0)) #fonga koiyu
    screen.blit(Rotated_R_h,R_hand_rotated_rect.topleft)
    screen.blit(Rotated_L_h,L_hand_rotated_rect.topleft)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

            


