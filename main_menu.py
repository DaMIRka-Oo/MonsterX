import pygame, sys
from pygame.locals import *
from Draw_Text import DrawText, drawText
from Fraction_Image import FractionImage, PlayingCard


mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 50)


click = False


def mainMenu():
    screen = pygame.display.set_mode((500, 400),0,32)
    while True:

        screen.fill((0,0,0))
        drawText('Monster X', pygame.font.SysFont(None, 50), (255, 255, 255), screen, 170, 20)

        drawText('Choose your side', pygame.font.SysFont(None, 30), (255, 255, 255), screen, 170, 80)

        mx, my = pygame.mouse.get_pos()

        image1 = FractionImage('DM logo.png', screen, 100, 80, 160, 190)
        image1.setByField()

        image2 = FractionImage('M logo.png', screen, 100, 80, 320, 190)
        image2.setByField()

        #textrect1=Draw_Text('Buy Full Version', pygame.font.SysFont(None, 20), (255, 255, 255), screen, 150, 300)
        #textrect1.set_by_field()

        textRect2=DrawText('Quit', pygame.font.SysFont(None, 40), (255, 255, 255), screen, 210, 300)
        textRect2.setByField()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        if image1.collide(mx, my, click):
            runUp(0)

        if image2.collide(mx, my, click):
            runUp(1)

        if textRect2.collide(mx, my, click):
            pygame.quit()
            sys.exit()

        pygame.display.update()
        mainClock.tick(60)



def runUp(num):
    Cards=[['DM1.jpg', 'DM2.jpg', 'DM3.jpg'], ['M1.jpg', 'M2.jpg', 'M3.jpg']]
    screen = pygame.display.set_mode((800, 470),0,32)
    running = True
    while running:
        screen.fill((0,0,0))

        drawText('Study your deck', font, (255, 255, 255), screen, 280, 20)

        mx, my = pygame.mouse.get_pos()

        Images = [FractionImage(Cards[num][i], screen, 222, 300, 160 + i*250, 220) for i in range(len(Cards[num]))]
        for im in Images:
            im.setByField()

        textRect1=DrawText('Start Buttle', pygame.font.SysFont(None, 50), (255, 255, 255), screen, 200, 400)
        textRect1.setByField()

        textRect2=DrawText('Back', pygame.font.SysFont(None, 30), (255, 255, 255), screen, 700, 400)
        textRect2.setByField()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if textRect1.collide(mx, my, click):
            game(num)

        if textRect2.collide(mx, my, click):
            mainMenu()

        pygame.display.update()
        mainClock.tick(60)


def game(num):
    Cards=[['DM1.jpg', 'DM2.jpg', 'DM3.jpg'], ['M1.jpg', 'M2.jpg', 'M3.jpg']]
    screen = pygame.display.set_mode((1000, 600),0,32)
    running = True
    bg = pygame.image.load("Background.png")
    bg = pygame.transform.scale(bg, (1000, 600))
    nums=[0,0,0]
    picked=[False, False, False]
    pos=[-1,-1,-1]
    cardChoosed=False
    choosed=[0,0,0]
    click=False
    cardsOnClose=0
    cardsOnDistance=0
    while running:
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        #draw_text('Study your deck', font, (255, 255, 255), screen, 280, 20)

        mx, my = pygame.mouse.get_pos()

        myCards = [PlayingCard(Cards[num][i], screen, 111, 150, i, nums[i], picked[i], pos[i]) for i in range(len(Cards[num]))]
        for im in myCards:
            im.setByField()

        image1 = FractionImage('Close combat.png', screen, 115, 148, 490, 375)
        image2 = FractionImage('Distant buttle.png', screen, 115, 145, 485, 518)
        if cardChoosed:
            image1.setByField()

            image2.setByField()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        for im in myCards:
            state, number=im.collide(mx, my, click)
            choosed[number]=[0,0,0]
            if state:
                cardChoosed=True
                choosed[number]=1



        if image1.collide(mx, my, click) and cardChoosed:
            for i in range(len(choosed)):
                if i==1:
                    number=i
            cardChoosed=False
            picked[number]=True
            pos[number]=0
            nums[number]=cardsOnClose
            cardsOnClose+=1

        if image2.collide(mx, my, click) and cardChoosed:
            cardChoosed=False
            picked[number]=True
            pos[number]=1
            nums[number]=cardsOnDistance
            cardsOnDistance+=1


        pygame.display.update()
        mainClock.tick(60)

mainMenu()
