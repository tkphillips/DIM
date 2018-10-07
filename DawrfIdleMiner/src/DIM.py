import pygame, sys, time, os
from pygame.locals import*

pygame.init()
pygame.font.init()
#window size and title
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Dwarf Idle Miner')
#clock
clock = pygame.time.Clock()
#colors
BACKGROUND_COLOR = (237, 225, 192)
LIGHT_GRAY = (120, 120, 120)
BLACK = (0,0,0)
myfont = pygame.font.SysFont("monospace", 16)

#Sprite Import
imgProgressBarOutline = pygame.image.load("Sprites\Progressbaroutline384x90.png")
imgProgressBar = pygame.image.load("Sprites\progressBar312x30.png")
# dwarfImg = pygame.image,load('filename')
#spritesize
#dwarfx=
#dwarfy=
#Variables
maxWidth = 312
defaultTime = 5
modifier = 1
timeFull = defaultTime * modifier
coefficient = maxWidth / timeFull
timeProgress = 0
dt = 0
globalTime = 0
gCount = 0
baseGoldRate = 1
goldModifier = 1
outlineProgresBarx = 30
outlineProgresBary = 100

#functions
#def progressBar(defaultTime, modifier ):

def mining(Miner, Materials):
    Materials.wood = Miner.num * .01
    Materials.iron = Miners.num * .05

class Materials:
    Floor(wood) = 0
    Floor(iron) = 0
class Miner:
    num = 0
    costRate = 1.07
    cost = 10 * costRate**num
    def buy_miner(self):
        Miner.num = Miner.num + 1
        global gCount
        gCount = gCount - Miner.cost
        return
    def num_miner(self):
        return Miner.num


# main game loop
while True:

    miner = Miner()
    materials = Materials()


    #globalTime += dt

    if timeProgress < timeFull:
        timeProgress += dt
        width = timeProgress * coefficient
        if timeProgress >= timeFull:
            width = 0
            timeProgress = 0
            if timeFull >= .01:
                modifier = modifier * .9
                timeFull = defaultTime * modifier
                coefficient = maxWidth / timeFull
                width = timeProgress * coefficient
            else:
                modifier = modifier * .9
                timeFull = defaultTime * modifier
                width = maxWidth
            goldModifier = goldModifier * 1.2
            gCount = gCount + (baseGoldRate * goldModifier)

    if gCount >= 10:
        miner.buy_miner()


    #push
    croppedProgress = pygame.Surface((width, 30))
    #drawBackground
    screen.fill(BACKGROUND_COLOR)
    #draw text
    goldText = myfont.render("Gold: {0}".format(int(gCount)), 1, (0,0,0))
    modifierText = myfont.render("Modifier: {0}".format((1/modifier)), 1, (0,0,0))
    minerText = myfont.render("Miners: {0}".format(miner.num), 1, (0,0,0))
    screen.blit(modifierText, (5, 30))
    screen.blit(goldText, (5, 10))
    screen.blit(minerText, (5,50))
    #drawSprites
    #pygame.draw.rect(screen, LIGHT_GRAY, (51, 100,width, 80))
    #screen.blit(imgProgressBar, (70,150))
    croppedProgress.blit(imgProgressBar,(0,0))
    screen.blit(croppedProgress, (outlineProgresBarx + 36 ,outlineProgresBary + 30))
    screen.blit(imgProgressBarOutline, (outlineProgresBarx,outlineProgresBary))
    #display update
    pygame.display.update()
    #clock update
    dt = clock.tick(60) / float(1000)

    #exit loop
    for event in pygame.event.get():
        #check quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
