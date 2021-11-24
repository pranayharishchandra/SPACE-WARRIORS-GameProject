import pygame
pygame.init()
x = pygame.display.set_mode((850,850))
pygame.display.set_caption('emoji game')
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

