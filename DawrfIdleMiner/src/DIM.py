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
BACKGROUND_COLOR = (222,184,135)
LIGHT_GRAY = (120, 120, 120)
BLACK = (0,0,0)
myfont = pygame.font.SysFont("monospace", 16)

#Sprite Import
imgButton = pygame.image.load("Sprites\Button96x48.png")
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
baseGoldRate = 10
goldModifier = 1
outlineProgresBarx = 100
outlineProgresBary = 150
woodCost = 5

#functions
#def progressBar(defaultTime, modifier ):



class Materials:
    wood = 0
    iron = 0
class Miner:
    num = 1
    costRate = 1.07
    cost = 10 * (costRate**(num-1))
    def buy_miner(self):
        Miner.num = Miner.num + 1
        global gCount
        gCount = gCount - Miner.cost
        Miner.cost = 10 * (Miner.costRate**Miner.num)
        return
    def num_miner(self):
        return Miner.num

def mining(Miner, Materials):
    Materials.wood += Miner.num * 1
    Materials.iron += Miner.num * .5



# main game loop
while True:

    miner = Miner()
    materials = Materials()




    #globalTime += dt

    #mining


    #Progress bar loop
    if timeProgress < timeFull:
        timeProgress += dt
        timeFull = defaultTime * modifier
        coefficient = maxWidth / timeFull
        width = timeProgress * coefficient
        if timeProgress >= timeFull:
            width = 0
            timeProgress = 0
            if timeFull >= .01:
                width = timeProgress * coefficient
            else:
                width = maxWidth
            mining(Miner, Materials)

    # buy miner button loop
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 300 + 96 > mouse[0] > 300 and 300 + 48 > mouse[1] > 300:
        if click[0] == 1 and gCount >= miner.cost:
            miner.buy_miner()

    #sell Wood Button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 150 + 96 > mouse[0] > 150 and 300 + 48 > mouse[1] > 300:
        if click[0] == 1 and materials.wood > 1:
            materials.wood = materials.wood - 1
            gCount = gCount + woodCost


    #push
    croppedProgress = pygame.Surface((width, 30))
    #drawBackground
    screen.fill(BACKGROUND_COLOR)
    #draw text
    goldText = myfont.render("Gold: {0}".format(int(gCount)), 1, (0,0,0))
    modifierText = myfont.render("Modifier: {0}".format((1/modifier)), 1, (0,0,0))
    minerText = myfont.render("Miners: {0}".format(miner.num), 1, (0,0,0))
    woodText = myfont.render("Wood: {0}".format(materials.wood), 1, (0,0,0))
    ironText = myfont.render("Iron: {0}".format(materials.iron), 1, (0,0,0))
    buyMinerText = myfont.render("Buy Miner Gold: {0}".format(miner.cost), 1, (0,0,0))
    screen.blit(modifierText, (5, 30))
    screen.blit(goldText, (5, 10))
    screen.blit(minerText, (5,50))
    screen.blit(woodText, (5, 70))
    screen.blit(ironText, (5, 90))
    screen.blit(buyMinerText, (5, 110))
    #drawSprites
    croppedProgress.blit(imgProgressBar,(0,0))
    screen.blit(croppedProgress, (outlineProgresBarx + 36 ,outlineProgresBary + 30))
    screen.blit(imgProgressBarOutline, (outlineProgresBarx,outlineProgresBary))
    screen.blit(imgButton, (300,300))
    screen.blit(imgButton, (150,300))
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
