import pygame

#to initialize
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600)) #TWO BRACKETS HERE

#TITEL AND ICON
pygame.display.set_caption('Space Warriors')#use 32*32 for icons
# icon = pygame.image.load('spaceship_icon_32bits.png')
# pygame.display.set_icon(icon)


#GAME LOOP
running =True
while running: #this loop exits when closed button is pressed

    # pass   #this much will hang the window ... program is in while loop and never ends so now you have to add QUIT 
    #anyting happening inside game window is an event even pressing of close button is also an event in pygame
    #we hve to make sure we exit this loop when closed button is pressed
    #so make variable running = True
    for event in pygame.event.get():
        #this will manage all the events happening inside our game widow
        #if we press red cross then the while loop should exit and we can do that by making while False
        if event.type ==pygame.QUIT:#MAKE SURE YOU WRITE QUIT IN CAPITAL LETTERS
            running = False
            



