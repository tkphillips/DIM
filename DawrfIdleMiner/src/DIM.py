import pygame, sys, time, os, random
from pygame.locals import*

pygame.init()
pygame.font.init()
#Sprite Import
xMax=640
yMax=480
defaultX = 640
defaultY = 480
imgButton = pygame.image.load("Sprites\Button96x48.png")
imgBackground = pygame.image.load("Sprites\Background.png")
imgProgressBarOutline = pygame.image.load("Sprites\Progressbaroutline384x90.png")
imgProgressBar = pygame.image.load("Sprites\progressBar312x30.png")
imgButton = pygame.image.load("Sprites\Button96x48.png")
imgProgressBar = pygame.image.load("Sprites\progressBar312x30.png")
#window size and title
screen = pygame.display.set_mode((defaultX, defaultY), HWSURFACE|DOUBLEBUF|RESIZABLE) ##########################################
fake_screen = screen.copy()                                                             ##############################
pygame.display.set_caption('Dwarf Idle Miner')
screenSurface = pygame.Surface((defaultX,defaultY))
                          ########################################
imgBackgroundScaled = pygame.transform.scale(imgBackground, (defaultX,defaultY))
screenSurface.blit(imgBackgroundScaled, (0,0))


                                       ########################################
#clock
clock = pygame.time.Clock()
#colors
BACKGROUND_COLOR = (222,184,135)
LIGHT_GRAY = (120, 120, 120)
BLACK = (0,0,0)
myfont = pygame.font.SysFont("monospace", 16)


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
outlineProgresBarx = 40
outlineProgresBary = 340
down = False
enemyNum = 1


#def progressBar(defaultTime, modifier ):


#Classes
class Enviroment:
    zone = 0
    enemyHealth = 1  #scaling factor
    mine = 0
    
class Materials:
    gCount = 10
    wood = 0
    iron = 0
    ancientTech = 0
    woodCost = 1
    ironCost = 5
    def sell_wood(self):
        Materials.gCount += ( Materials.wood * Materials.woodCost)
        Materials.wood = 0
    def sell_iron(self):
        Materials.gCount += (Materials.iron * Materials.ironCost)
        Materials.iron = 0

class Miner:
    num = 1
    costRate = 1.07
    cost = 10 * (costRate**(num-1))
    def buy_miner(self):
        Miner.num = Miner.num + 1
        Materials.gCount = Materials.gCount - Miner.cost
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
        Materials.gCount -= Warrior.cost
        Warrior.cost = 10 * (Warrior.costRate**Warrior.num)
class Enemy:
    startHealth = random.randint(10,50)
    currHealth = startHealth
    def death(self):
        Materials.gCount += (Enemy.startHealth / 10)
        Enemy.startHealth = random.randint(10,50)
        Enemy.currHealth = Enemy.startHealth
    def do_damage(self, damage, num):
        Enemy.currHealth -= damage * num

#functions
def mining(Miner, Materials):
    Materials.wood += Miner.num * 1
    Materials.iron += Miner.num * .5

def scale(x,y):
    global xMax
    global defaultX
    global yMax
    global defaultY
    x = int( x *(xMax / defaultX))
    y = int(y *(yMax / defaultY))
    return(x,y)



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
            if enemy.currHealth <= 0:
                enemy.death()
            enemy.do_damage(warrior.damage, warrior.num)
            if enemy.currHealth <= 0:
                enemy.death()







    # buy miner button loop
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if scale(396,300)[0] > mouse[0] > scale(300,300)[0] and scale(300,348)[1] > mouse[1] > scale(300,300)[1]:
                if materials.gCount >= miner.cost and down == False:
                    miner.buy_miner()
                    down = True


    #sell Wood Button
            elif scale(246,0)[0] > mouse[0] > scale(150,0)[0] and scale(0,348)[1] > mouse[1] > scale(0,300)[1]:
               if materials.wood >= 1 and down == False:
                   materials.sell_wood()
                   down = True

       #sell iron Button
            elif scale(246,0)[0] > mouse[0] > scale(150,0)[0] and scale(0,423)[1] > mouse[1] > scale(0,375)[1]:
               if materials.iron >= 1 and down == False:
                   materials.sell_iron()
                   down = True
        #buy warrior
            elif scale(396,0)[0] > mouse[0] > scale(300,0)[0] and scale(0,423)[1] > mouse[1] >  scale(0,375)[1]:
               if materials.gCount >= warrior.cost and down == False:
                   warrior.buy_warrior()
                   down = True
       #unpress if statement
        elif event.type == pygame.MOUSEBUTTONUP:
                down = False
            #check quit
        elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Check Resize                                  ############################################
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
            fake_screen.blit(screenSurface, (100, 100))
            screen.blit(pygame.transform.scale(fake_screen, event.dict['size']), (0, 0))
            imgBackgroundScaled = pygame.transform.scale(imgBackground, event.dict['size'])
            xMax = event.dict['w']
            yMax = event.dict['h']
            pygame.display.flip()






    #drawBackground
    screen.blit(imgBackgroundScaled, (0,0))
    #surfaces
    croppedProgress = pygame.Surface((scale(width, 30)))
    imgProgressBarOutlineSurface = pygame.Surface(scale(384,90), pygame.SRCALPHA, 32)
    #scaling
    imgProgressBarOutlineScaled = pygame.transform.scale(imgProgressBarOutline, (scale(384,90)))
    imgProgressBarScaled = pygame.transform.scale(imgProgressBar, (scale(312,30)))
    imgButtonScaled = pygame.transform.scale(imgButton, (scale(96,48)))
    #draw text
    goldText = myfont.render("Gold: {0}".format(int(Materials.gCount)), 1, (0,0,0))
    modifierText = myfont.render("Modifier: {0}".format((1/modifier)), 1, (0,0,0))
    minerText = myfont.render("Miners: {0}".format(miner.num), 1, (0,0,0))
    warriorText = myfont.render("Warriors: {0}".format(warrior.num), 1, (0,0,0))
    woodText = myfont.render("Wood: {0}".format(materials.wood), 1, (0,0,0))
    ironText = myfont.render("Iron: {0}".format(int(materials.iron)), 1, (0,0,0))
    buyMinerText = myfont.render("Buy Miner Gold: {0:6.2f}".format(miner.cost), 1, (0,0,0))
    buyWarriorText = myfont.render("Buy Warrior Gold: {0:6.2f}".format(warrior.cost), 1, (0,0,0))
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
    croppedProgress.blit(imgProgressBarScaled,(0,0))
    screen.blit(croppedProgress, (scale(89,380)))
    imgProgressBarOutlineSurface.blit(imgProgressBarOutlineScaled, (0,0))
    screen.blit(imgProgressBarOutlineScaled, (scale(53,350)))
    screen.blit(imgButtonScaled, (scale(300,300)))
    screen.blit(imgButtonScaled, (scale(150,300)))
    screen.blit(imgButtonScaled, (scale(150,375)))
    screen.blit(imgButtonScaled, (scale(300,375)))
    #display update
    pygame.display.update()
    #clock update
    dt = clock.tick(60) / float(1000)
