import pygame

#to initialize
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600)) #TWO BRACKETS HERE #width,height #(x,y)

#TITEL AND ICON
pygame.display.set_caption('Space Warriors')#use 32*32 for icons
icon = pygame.image.load('spaceship_icon_32bits.png')
pygame.display.set_icon(icon)

#PLAYER ,  coordinates of player
player_image = pygame.image.load('plane_64bit.png')#don't forget to write png here
playerX = 360
playerY = 450

def player(x,y): #playerX has become x here and playerY has become y here ... and this x and y will go down ... uss din tu bhai toda confuse ho gya tha fir defination in python search kr k dekha tah yaad aaya 
    screen.blit(player_image, (x, y)) #blit basically means to draw  #put playerX, playerY  in bracket  (playerX, playerY)like this

'''place icon in the same folder where freecodecampgame.py is ... (don't put this inside some new folder )'''


#GAME LOOP
running =True
while running: #this loop exits when closed button is pressed

    #        RED GREEN BLUE -- these values goes from zero to 255
    screen.fill((0,0,0))


    playerX = playerX + 0.1

    #because screen comes first so we have written screen first ... then over it below things/images will get added so written below this

    # pass   #this much will hang the window ... program is in while loop and never ends so now you have to add QUIT 
    #anyting happening inside game window is an event even pressing of close button is also an event in pygame
    #we hve to make sure we exit this loop when closed button is pressed
    #so make variable running = True
    for event in pygame.event.get():
        #this will manage all the events happening inside our game widow
        #if we press red cross then the while loop should exit and we can do that by making while False
        if event.type ==pygame.QUIT:#MAKE SURE YOU WRITE QUIT IN CAPITAL LETTERS
            running = False

    player(playerX, playerY)
    pygame.display.update() # You have to write this to upadate anything and everything in the game window