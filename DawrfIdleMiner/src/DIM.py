import pygame, sys, time, os, random
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
gCount = 10
baseGoldRate = 10
goldModifier = 1
outlineProgresBarx = 100
outlineProgresBary = 150
woodCost = 5
ironCost = 10
down = False
enemyNum = 1


#def progressBar(defaultTime, modifier ):


#Classes
class Materials:
    wood = 0
    iron = 0
    def sell_wood(self):
        global gCount
        global woodCost
        gCount += woodCost
        Materials.wood -= 1
    def sell_iron(self):
        global gCount
        global ironCost
        gCount += ironCost
        Materials.iron -= 1
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

class Warrior:
    num = 0
    costRate = 1.07
    cost = 10 * (costRate**num)
    damage = 10
    def buy_warrior(self):
        Warrior.num += 1
        global gCount
        gCount -= Warrior.cost
        Warrior.cost = 10 * (Warrior.costRate**Warrior.num)
class Enemy:
    startHealth = random.randint(10,50)
    currHealth = startHealth
    def death(self):
        global gCount
        gCount += int(Enemy.startHealth % 10)
        Enemy.startHealth = random.randint(10,50)
        Enemy.currHealth = Enemy.startHealth
    def do_damage(self, damage, num):
        Enemy.currHealth -= damage * num

#functions
def mining(Miner, Materials):
    Materials.wood += Miner.num * 1
    Materials.iron += Miner.num * .5





# main game loop
while True:

    miner = Miner()
    materials = Materials()
    enemy = Enemy()
    warrior = Warrior()




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
            #Doing damage
<<<<<<< HEAD
=======
            if enemy.currHealth <= 0:
                enemy.death()
            enemy.do_damage(warrior.damage, warrior.num)
>>>>>>> 145389e0a66199cda4f948e7653f8244b5b5f733
            if enemy.currHealth <= 0:
                enemy.death()
            enemy.do_damage(warrior.damage, warrior.num)



            #Enemy


    # buy miner button loop
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 + 96 > mouse[0] > 300 and 300 + 48 > mouse[1] > 300:
                if gCount >= miner.cost and down == False:
                    miner.buy_miner()
                    down = True


    #sell Wood Button
            elif 150 + 96 > mouse[0] > 150 and 300 + 48 > mouse[1] > 300:
               if materials.wood >= 1 and down == False:
                   materials.sell_wood()
                   down = True

       #sell iron Button
            elif 150 + 96 > mouse[0] > 150 and 375 + 48 > mouse[1] > 375:
               if materials.iron >= 1 and down == False:
                   materials.sell_iron()
                   down = True
        #buy warrior
            elif 300 + 96 > mouse[0] > 300 and 375 + 48 > mouse[1] > 375:
               if gCount >= warrior.cost and down == False:
                   warrior.buy_warrior()
                   down = True
       #unpress if statement
        elif event.type == pygame.MOUSEBUTTONUP:
                down = False
            #check quit
        elif event.type == QUIT:
                pygame.quit()
                sys.exit()






    #push
    croppedProgress = pygame.Surface((width, 30))
    #drawBackground
    screen.fill(BACKGROUND_COLOR)
    #draw text
    goldText = myfont.render("Gold: {0}".format(int(gCount)), 1, (0,0,0))
    modifierText = myfont.render("Modifier: {0}".format((1/modifier)), 1, (0,0,0))
    minerText = myfont.render("Miners: {0}".format(miner.num), 1, (0,0,0))
    warriorText = myfont.render("Warriors: {0}".format(warrior.num), 1, (0,0,0))
    woodText = myfont.render("Wood: {0}".format(materials.wood), 1, (0,0,0))
    ironText = myfont.render("Iron: {0}".format(int(materials.iron)), 1, (0,0,0))
    buyMinerText = myfont.render("Buy Miner Gold: {0}".format(miner.cost), 1, (0,0,0))
    buyWarriorText = myfont.render("Buy Warrior Gold: {0}".format(warrior.cost), 1, (0,0,0))
    emenyHealthText = myfont.render("Enemy Health: {0}".format(enemy.currHealth), 1, (0,0,0))
    screen.blit(modifierText, (5, 30))
    screen.blit(emenyHealthText, (200, 30))
    screen.blit(goldText, (5, 10))
    screen.blit(minerText, (5,50))
    screen.blit(woodText, (5, 70))
    screen.blit(ironText, (5, 90))
    screen.blit(buyMinerText, (5, 110))
    screen.blit(buyWarriorText, (250, 110))
    screen.blit(warriorText, (130, 50))
    #drawSprites
    croppedProgress.blit(imgProgressBar,(0,0))
    screen.blit(croppedProgress, (outlineProgresBarx + 36 ,outlineProgresBary + 30))
    screen.blit(imgProgressBarOutline, (outlineProgresBarx,outlineProgresBary))
    screen.blit(imgButton, (300,300))
    screen.blit(imgButton, (150,300))
    screen.blit(imgButton, (150,375))
    screen.blit(imgButton, (300,375))
    #display update
    pygame.display.update()
    #clock update
    dt = clock.tick(60) / float(1000)
