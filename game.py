from bisect import bisect_left
import Fighter
import HardCom
import pygame
import random
from random import randint
import sys


# init pygame module
pygame.init()

# set display characteristics
display_width = 1280
display_height = 720
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ApMathFighters')

# icons
icon = pygame.image.load('image')
pygame.display.set_icon(surface)

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
tomato = (255, 99, 71)
coral=(255, 127, 80)
orangered=(255, 69, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# number of frames per second 
FPS = 24
FPSClock = pygame.time.Clock()

# text characteristics
titlefont = pygame.font.Font('fonts/GOODTIME.ttf', 64)
msgfont = pygame.font.Font('fonts/GOODTIME.ttf', 32)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("", 50)
largefont = pygame.font.SysFont("comicsansms", 85)
codefont = pygame.font.SysFont("comicsansms", 20)
copyrfont = pygame.font.SysFont("comicsansms", 18)


# text display functions 
def text_objects(text, color, type="small"):
    if type == "title":
        textSurface = titlefont.render(text, True, color)
    if type == "small":
        textSurface = smallfont.render(text, True, color)
    if type == "medium":
        textSurface = medfont.render(text, True, color)
    if type == "large":
        textSurface = largefont.render(text, True, color)
    if type == "code":
        textSurface = codefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, type="small"):
    textSurf, textRect = text_objects(msg, color, type)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


# initializations of players
fighter1_sprites = (
    'fighters/fighter1/00.png', 'fighters/fighter1/01.png', 'fighters/fighter1/02.png', 'fighters/fighter1/03.png',
    'fighters/fighter1/11.png', 'fighters/fighter1/12.png',
    'fighters/fighter1/13.png', 'fighters/fighter1/21.png', 'fighters/fighter1/22.png', 'fighters/fighter1/23.png')
fighter2_sprites = (
    'fighters/fighter2/00.png', 'fighters/fighter2/01.png', 'fighters/fighter2/02.png', 'fighters/fighter2/03.png',
    'fighters/fighter2/11.png', 'fighters/fighter2/12.png',
    'fighters/fighter2/13.png', 'fighters/fighter2/21.png', 'fighters/fighter2/22.png', 'fighters/fighter2/23.png')

# initializations background images 
backgrounds = ["backgrounds/background1.jpg", "backgrounds/background2.jpg", "backgrounds/background3.jpg",
               "backgrounds/background4.jpg", "backgrounds/background5.jpg"]
background1 = pygame.image.load(backgrounds[random.randrange(0, 5)]).convert()
message1 = pygame.image.load("backgrounds/message1.jpg").convert()
message2 = pygame.image.load("backgrounds/message2.jpg").convert()
message3 = pygame.image.load("backgrounds/message3.jpg").convert()

# initializations of the first player 
fighter1 = Fighter(300, 200, fighter1_sprites)
fighter1.isplayerone = True
# создание второго игрока
fighter2 = Fighter(display_width - 300 - 400, 200, fighter2_sprites)
fighter2.isplayerone = False


""" Players options """

# function of choosing an option by a computer player
# difficulty level: easy 
def easyCom():
    options = ('high', 'mid', 'low', 'nc')
    compChoice = random.choice(options)
    return compChoice


# function of choosing an option by a computer player
# difficulty level: normal 
def normalCom():
    options = ('high', 'mid', 'low')
    compChoice = random.choice(options)
    return compChoice


# function of choosing an option by a computer player
# difficulty level: high 
def weighted_choice(values, weights):
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect_left(cum_weights, x)
    return values[i]


# health quantity display function 
def healthbar(player1_health, player2_health):
    if player1_health > 9:
        player1_hcolor = green
    elif player1_health > 4:
        player1_hcolor = yellow
    else:
        player1_hcolor = red
    if player2_health > 9:
        player2_hcolor = green
    elif player2_health > 4:
        player2_hcolor = yellow
    else:
        player2_hcolor = red
    pygame.draw.rect(gameDisplay, black, (15, 20, 510, 35))
    pygame.draw.rect(gameDisplay, black, (755, 20, 510, 35))
    if player1_health > 0:
        pygame.draw.rect(gameDisplay, player1_hcolor, (20, 25, player1_health * 25, 25))
    if player2_health > 0:
        pygame.draw.rect(gameDisplay, player2_hcolor, (1280 - 20 - player2_health * 25, 25, player2_health * 25, 25))


# flash draw function 
def explosion(x, y, size=50):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        colorChoices = [red, orangered, tomato, coral]
        magnitude = 1
        while magnitude < size:
            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)], (exploding_bit_x,exploding_bit_y),random.randrange(10,15))
            magnitude += 1
            pygame.display.update()
            FPSClock.tick(FPS)
        explode = False

# timer color change function 
def timercolor(originalTime):
    if originalTime < 6:
        return red
    else:
        return blue


# pause function 
def pause():
    paused = True
    message_to_screen("PAUSED", blue, 0)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        FPSClock.tick(FPS)


# main menu of the game 
def gameMenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu = False
                    fight()
                if event.key == pygame.K_d:
                    menu = False
                    fight("human")
                elif event.key == pygame.K_s:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)
        message_to_screen("ApMath Fighters", blue, -250, "title")
        gameDisplay.blit(msgfont.render("Arcade", True, blue), (700, 300))
        gameDisplay.blit(msgfont.render("Versus", True, blue), (700, 350))
        gameDisplay.blit(msgfont.render("Quit", True, blue), (700, 400))
        fighter1.update()
        fighter1.draw(gameDisplay)
        pygame.display.update()
        FPSClock.tick(FPS)


""" Game process """

def fight(opponent="normal"):
    player1_loses = False
    player2_loses = False
    players_draw = False
    originalTime = 33
    player1_health = 20
    player2_health = 20
    endframe = 0
    playersChoice = 'mid'
    computersChoice = 'mid'
    player2Choice = 'mid'
    if opponent == 'hard':
        com = hardCom()
        computersChoice = com.predict()
    isfight = True
    while isfight:

        # set a timer for the players' turn 
        if originalTime != -1:
            originalTime -= 1
        else:
            originalTime = 33
        displayingTime = str(originalTime + 1)

        # reading the first player's keystrokes 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # the task of choosing the first player 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    playersChoice = 'mid'
                if event.key == pygame.K_w:
                    playersChoice = 'high'
                if event.key == pygame.K_s:
                    playersChoice = 'low'
                if event.key == pygame.K_LEFT:
                    player2Choice = 'mid'
                if event.key == pygame.K_UP:
                    player2Choice = 'high'
                if event.key == pygame.K_DOWN:
                    player2Choice = 'low'
        if originalTime % 100 == 0:

            # the task of choosing a second player 
            if opponent == "easy":
                computersChoice = easyCom()
            elif opponent == "normal":
                computersChoice = normalCom()
            elif opponent == "hard":
                com.store(playersChoice)
                computersChoice = com.predict()
            elif opponent == "human":
                computersChoice = player2Choice

            # possible options for the events of the game 
            if (playersChoice == 'high') and (computersChoice == 'high'):
                fighter1.hpc = True
                fighter2.hpc = True
                player1_health -= 1
                player2_health -= 1
            if (playersChoice == 'high') and (computersChoice == 'mid'):
                fighter1.hp = True
                fighter2.mpc = True
                player2_health -= 1
            if (playersChoice == 'high') and (computersChoice == 'low'):
                fighter1.hpc = True
                fighter2.lp = True
                player1_health -= 1
            if (playersChoice == 'mid') and (computersChoice == 'high'):
                fighter1.mpc = True
                fighter2.hp = True
                player1_health -= 1
            if (playersChoice == 'mid') and (computersChoice == 'mid'):
                fighter1.mpc = True
                fighter2.mpc = True
                player1_health -= 1
                player2_health -= 1
            if (playersChoice == 'mid') and (computersChoice == 'low'):
                fighter1.mp = True
                fighter2.lpc = True
                player2_health -= 1
            if (playersChoice == 'low') and (computersChoice == 'high'):
                fighter1.lp = True
                fighter2.hpc = True
                player2_health -= 1
            if (playersChoice == 'low') and (computersChoice == 'mid'):
                fighter1.lpc = True
                fighter2.mp = True
                player1_health -= 1
            if (playersChoice == 'low') and (computersChoice == 'low'):
                fighter1.lpc = True
                fighter2.lpc = True
                player1_health -= 1
                player2_health -= 1
            if (playersChoice == 'nc') and (computersChoice == 'high'):
                fighter1.mpc = True
                fighter2.hp = True
                player1_health -= 1
            if (playersChoice == 'nc') and (computersChoice == 'mid'):
                fighter1.mpc = True
                fighter2.mp = True
                player1_health -= 1
            if (playersChoice == 'nc') and (computersChoice == 'low'):
                fighter1.mpc = True
                fighter2.hp = True
                player1_health -= 1
            if (playersChoice == 'high') and (computersChoice == 'nc'):
                fighter1.hp = True
                fighter2.mpc = True
                player2_health -= 1
            if (playersChoice == 'mid') and (computersChoice == 'nc'):
                fighter1.mp = True
                fighter2.mpc = True
                player2_health -= 1
            if (playersChoice == 'low') and (computersChoice == 'nc'):
                fighter1.lp = True
                fighter2.mpc = True
                player2_health -= 1
            print(playersChoice, computersChoice, player1_health, player2_health)

        # conditions at the end of the fight 
        if player1_health == 0 or player2_health == 0:
            endframe += 1
        if (player1_health == 0) and (player2_health != 0) and endframe > 11:
            player1_loses = True
            isfight = False
            continue
        elif (player1_health != 0) and (player2_health == 0) and endframe > 10:
            player2_loses = True
            isfight = False
            continue
        elif (player1_health == 0) and (player2_health == 0) and endframe > 10:
            players_draw = True
            isfight = False
            continue

        # background image display 
        gameDisplay.blit(background1, (0, 0))

        # drawing health bars 
        healthbar(player1_health, player2_health)

        # drawing timer 
        message_to_screen(displayingTime, timercolor(originalTime), -320, "title")

        # drawing players 
        fighter1.update()
        fighter1.draw(gameDisplay)
        fighter2.update()
        fighter2.draw(gameDisplay)

        # updating the screen image 
        FPSClock.tick(FPS)
        pygame.display.update()
    if player1_loses:
        print("Player 2 wins!")
        player2_winmessage()
    if player2_loses:
        print("Player 1 wins!")
        player1_winmessage()
    if players_draw:
        print("Draw!")
        draw_winmessage()


# first player win message 
def player1_winmessage():
    p1message = True
    while p1message:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        gameDisplay.blit(message1, (0,0))
        pygame.display.update()
        FPSClock.tick(FPS)


# message about the win of the second player 
def player2_winmessage():
    p2message = True
    while p2message:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        gameDisplay.blit(message2, (0,0))
        pygame.display.update()
        FPSClock.tick(FPS)


# draw message 
def draw_winmessage():
    p3message = True
    while p3message:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        gameDisplay.blit(message3, (0,0))
        pygame.display.update()
        FPSClock.tick(FPS)


gameMenu()