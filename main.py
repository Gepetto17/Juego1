#!/usr/bin/env python3

# Libraries import
import pygame
from pygame.locals import *
import random

# Variables declaration
size = width, height = (1200, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = int(width/2.0 + road_w/4.0)
left_lane = int(width/2.0 - road_w/4.0)
speed = 1

# Initialize
pygame.init()
running = True

# Set window size
screen = pygame.display.set_mode(size)

# Set title
pygame.display.set_caption("Virginity_keeper")

# Set background color
screen.fill((60,220,0))

# Apply changes
pygame.display.update()

# Load images
concha = pygame.image.load("Concha.png")
concha_loc = concha.get_rect()
concha_loc.center = right_lane, int(height*0.8)

pingo = pygame.image.load("Pingo.png")
pingo_loc = pingo.get_rect()
pingo_loc.center = left_lane, int(height*0.2)

counter = 0
while running:
    counter += 1
    if counter == 2000:
        speed += 0.15
        counter = 0
        print("LEVEL UP!", speed)
    # Animate enemy pingo
    pingo_loc[1] += speed
    if pingo_loc[1] > height:
        if random.randint(0,1) == 0:
            pingo_loc.center = right_lane, -200
        else:
            pingo_loc.center = left_lane, -200
    
    # End game condition
    if concha_loc[0] == pingo_loc[0] and pingo_loc[1] > concha_loc[1] - 100:
        print("GAME OVER! YOU'VE BEEN BONED")
        break
    
    # Event listener
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
            	if event.key in [K_a, K_LEFT] and concha_loc[0] > left_lane:
            	    concha_loc = concha_loc.move([-int(road_w/2.0), 0])
            	if event.key in [K_d, K_RIGHT] and concha_loc[0] < left_lane:
            	    concha_loc = concha_loc.move([int(road_w/2.0), 0])
    pygame.draw.rect(
        screen, # Where to draw
        (100, 100, 100), # Color
        (int(width/2.0 - road_w/2.0), 0, road_w, height)) # (X value from the left, Y value from the top, Width of the shape, Height of the shape)
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (int(width/2.0 - roadmark_w/2.0), 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (int(width/2.0 - road_w/2.0 + roadmark_w*2.0), 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (int(width/2.0 + road_w/2.0 - roadmark_w*3.0), 0, roadmark_w, height))
    
    
    screen.blit(concha, concha_loc)
    screen.blit(pingo, pingo_loc)
    pygame.display.update()

pygame.quit()
