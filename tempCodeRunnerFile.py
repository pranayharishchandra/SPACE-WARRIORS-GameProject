import pygame
import random

# to initialize
pygame.init()

# create the screen
# TWO BRACKETS HERE #width,height #(x,y)
screen = pygame.display.set_mode((800, 600))

# TITEL AND ICON
pygame.display.set_caption('Space Warriors')  # use 32*32 for icons
icon = pygame.image.load('spaceship_icon_32bits.png')
pygame.display.set_icon(icon)

# PLAYER ,  coordinates of player
# don't forget to write png here
player_image = pygame.image.load('plane_64bit.png')
playerX = 360
playerY = 450
playerX_change = 0
playerY_change = 0

# ADDING ALIEN
alien_image = pygame.image.load('aliens.png')  # don't forget to write png here
alienX = random.randint(0,736)
alienY = random.randint(10,100)
alienX_change = 0.2
alienY_change = 40


def player(x, y):  # playerX has become x here and playerY has become y here ... and this x and y will go down ... uss din tu bhai toda confuse ho gya tha fir defination in python search kr k dekha tah yaad aaya
    # blit basically means to draw  #put playerX, playerY  in bracket  (playerX, playerY)like this
    screen.blit(player_image, (x, y))


def alien(x, y):
    screen.blit(alien_image, (x, y))

#'''place icon in the same folder where freecodecampgame.py is ... (don't put this inside some new folder )'''


# GAME LOOP
running = True
while running:  # this loop exits when closed button is pressed

    #        RED GREEN BLUE -- these values goes from zero to 255
    screen.fill((0, 0, 0))

    # '''playerX = playerX + 0.1 #adding 0.1 in x so image will move RHS'''

    # because screen comes first so we have written screen first ... then over it below things/images will get added so written below this

    # pass   #this much will hang the window ... program is in while loop and never ends so now you have to add QUIT
    # anyting happening inside game window is an event even pressing of close button is also an event in pygame
    # we have to make sure we exit this loop when closed button is pressed
    # so make variable running = True
    for event in pygame.event.get():
        # this will manage all the events happening inside our game widow
        # if we press red cross then the while loop should exit and we can do that by making while False
        if event.type == pygame.QUIT:  # MAKE SURE YOU WRITE QUIT IN CAPITAL LETTERS
            running = False
            break

        if event.type == pygame.KEYDOWN:  # key down  means pressing the key and key up means releasing the key
            # print('A key is pressed')
            if event.key == pygame.K_LEFT:
                #print('LEFT arrow is pressed')
                playerX_change = -0.6

            if event.key == pygame.K_RIGHT:
                # print('RIGHT arrow is pressed')
                playerX_change = 0.6

        if event.type == pygame.KEYUP:          # releasing the key ... which was either right or left
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # speed of  spaceship AFTER RELESING THE KEY #if you don't write this or pass and leave it empty then you will get error since conditional statements need something REMEMBER HAHA

                #  print('keystroke has been released')


#    PLAYER
    playerX = playerX + playerX_change
    # playerY = playerY + playerY_change

    # ADDING BOUNDARIES FOR OUR SPACESHIP
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800-64=736
        playerX = 736

#    ALIEN
    # alienX = alienX + alienX_change
    # ADDING BOUNDARIES FOR OUR ALIEN
    if alienX <= 0:
        alienX_change = 0.2
        alienY = alienY + alienY_change

    elif alienX >= 736:  # 800-64=736
        alienX_change = -0.2
        alienY = alienY + alienY_change


    alienX = alienX + alienX_change

    player(playerX, playerY)
    alien(alienX, alienY)
    # You have to write this to upadate anything and everything in the game window
    pygame.display.update()
