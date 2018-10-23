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
imgMine = pygame.image.load("Sprites\Basic_cave64x49.png")
imgIcon = pygame.image.load("Sprites\DwarfMiner72x66.png")
enemySprt = pygame.image.load("Sprites\enemy_1.png")
imgWoodenPickaxe = pygame.image.load("Sprites\woodenpickaxe.png")
imgIronPickaxe = pygame.image.load("Sprites\ironpickaxe.png")
#window size and title
screen = pygame.display.set_mode((defaultX, defaultY), HWSURFACE|DOUBLEBUF|RESIZABLE)
fake_screen = screen.copy()
pygame.display.set_caption('Dwarf Idle Miner')
screenSurface = pygame.Surface((defaultX,defaultY))
imgBackgroundScaled = pygame.transform.scale(imgBackground, (defaultX,defaultY))
screenSurface.blit(imgBackgroundScaled, (0,0))
pygame.display.set_icon(imgIcon)



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

#GlobalVariables
down = False
modifier = 1

#Classes
#Class to manage prgression and Prestige
class Enviroment:
    zone = 0
    enemyHealth = 1  #scaling factor
    mine = 0
class Modifiers:  #class to add buffs to Warriors and Miners
    miner1 = True
    woodenPickaxe = False
    def buy_woodenPick(self):
        Materials.wood = Materials.wood - Materials.woodenPickaxeCost
        Modifiers.woodenPickaxe = True
        Timebar.modifier = timebar.modifier * .5
#Class To manage inventory
class Materials:
    gCount = 10
    wood = 0
    iron = 0
    ancientTech = 0
    woodCost = 1
    ironCost = 5
    woodenPickaxeCost = 15
    def sell_wood(self):   #Sell all button
        Materials.gCount += ( Materials.wood * Materials.woodCost)
        Materials.wood = 0
    def sell_iron(self):   #Sell all button
        Materials.gCount += (Materials.iron * Materials.ironCost)
        Materials.iron = 0

#Class to manage Miner
class Miner:
    num = 1
    costRate = 1.1   #Exponential factor used to calculate cost increase per miner purchased
    cost = 10   #Baseprice
    woodPro = 1
    ironPro = .5
    if Modifiers.miner1 == True:
        woodPro *= 1.05
        ironPro *= 1.05
    def buy_miner(self):
        Miner.num = Miner.num + 1
        Materials.gCount = Materials.gCount - Miner.cost
        Miner.cost = 10 * (Miner.costRate**Miner.num) #New cost after purchase
        return
    def num_miner(self):
        return Miner.num

class Warrior:
    num = 5
    costRate = 1.07
    cost = 10
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
        self.switch_sprite()
    def do_damage(self, damage, num):
        Enemy.currHealth -= damage * num
    def switch_sprite(self):
        spNm = random.randint(1,2)
        global enemySprt
        global enemyScaled
        enemySprt = pygame.image.load("Sprites\enemy_%d.png" % spNm)
        enemyScaled = pygame.transform.scale(enemySprt, (scale(100, 100)))
        mineSurface.blit(imgMineScaled,(0,0))
        screen.blit(mineSurface, (scale(330,60)))
        screen.blit(enemyScaled, (scale(452, 155)))

class Timebar:
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
    completion = 0
    width = 0
    def timeloop(self):
        if Timebar.timeProgress < Timebar.timeFull:
            Timebar.timeProgress += Timebar.dt
            Timebar.timeFull = Timebar.defaultTime * Timebar.modifier
            Timebar.coefficient = Timebar.maxWidth / Timebar.timeFull
            Timebar.width = Timebar.timeProgress * Timebar.coefficient
            Timebar.dt = clock.tick(60) / float(1000)
            if Timebar.timeProgress >= Timebar.timeFull:
                Timebar.width = 0
                Timebar.timeProgress = 0
                if Timebar.timeFull >= .01:
                    Timebar.width = Timebar.timeProgress * Timebar.coefficient
                else:
                    Timebar.width = Timebar.maxWidth
                Timebar.completion = 1
    def loopReset(self):
        Timebar.completion = 0
#functions
def mining(Miner, Materials):
    Materials.wood += Miner.num * Miner.woodPro
    Materials.iron += Miner.num * Miner.ironPro

#funciton for scaling sprites
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
    timebar = Timebar()
    modifiers = Modifiers()
    timebar.timeloop()


    #Functions that rely on progress bar completion
    if timebar.completion == 1:
        mining(Miner, Materials)
        #Doing damage
        if enemy.currHealth > 0:
            enemy.do_damage(warrior.damage, warrior.num)
        if enemy.currHealth <= 0:
            enemy.death()
        timebar.loopReset()







    # buy miner button loop
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if scale(526,0)[0] > mouse[0] > scale(430,0)[0] and scale(0,368)[1] > mouse[1] > scale(0,320)[1]:
                if materials.gCount >= miner.cost and down == False:
                    miner.buy_miner()
                    down = True


    #sell Wood Button
            elif scale((540+96),0)[0] > mouse[0] > scale(540,0)[0] and scale(0,(400+48))[1] > mouse[1] >  scale(0,400)[1]:
               if materials.wood >= 1 and down == False:
                   materials.sell_wood()
                   down = True

       #sell iron Button
            elif scale((430+96),0)[0] > mouse[0] > scale(430,0)[0] and scale(0,(400+48))[1] > mouse[1] > scale(0,400)[1]:
               if materials.iron >= 1 and down == False:
                   materials.sell_iron()
                   down = True
        #buy warrior
            elif scale((540+96),0)[0] > mouse[0] > scale(540,0)[0] and scale(0,(320+48))[1] > mouse[1] > scale(0,320)[1]:
               if materials.gCount >= warrior.cost and down == False:
                   warrior.buy_warrior()
                   down = True
        #make wooden Pickaxe
            elif scale((150+49),0)[0] > mouse[0] > scale(150,0)[0] and scale(0,(427+24))[1] > mouse[1] > scale(0,427)[1]:
               if materials.wood >= materials.woodenPickaxeCost and down == False and modifiers.woodenPickaxe == False:
                   modifiers.buy_woodenPick()
                   down = True
       #unpress if statement
        elif event.type == pygame.MOUSEBUTTONUP:
                down = False
            #check quit
        elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Check Resize
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
    croppedProgress = pygame.Surface((scale(timebar.width, 30)))
    imgProgressBarOutlineSurface = pygame.Surface(scale(384,90), pygame.SRCALPHA, 32)
    mineSurface = pygame.Surface((scale(300, 200)))
    button1Surface = pygame.Surface((scale(96, 48)))
    button2Surface = pygame.Surface((scale(96, 48)))
    button3Surface = pygame.Surface((scale(96, 48)))
    button4Surface = pygame.Surface((scale(96, 48)))
    button5Surface = pygame.Surface((scale(49, 24)))
    woodenPickaxeSurface = pygame.Surface(scale(32,32), pygame.SRCALPHA, 32)
    #scaling
    imgProgressBarOutlineScaled = pygame.transform.scale(imgProgressBarOutline, (scale(384,90)))
    imgProgressBarScaled = pygame.transform.scale(imgProgressBar, (scale(312,30)))
    imgButtonScaled = pygame.transform.scale(imgButton, (scale(96,48)))
    imgButtonScaledSmall = pygame.transform.scale(imgButton, (scale(49,24)))
    imgMineScaled = pygame.transform.scale(imgMine, (scale(300,200)))
    enemyScaled = pygame.transform.scale(enemySprt, (scale(100, 100)))
    woodenPickaxeScaled = pygame.transform.scale(imgWoodenPickaxe, (scale(32, 32)))
    #drawSprites
    mineSurface.blit(imgMineScaled,(0,0))
    screen.blit(mineSurface, (scale(330,60)))
    croppedProgress.blit(imgProgressBarScaled,(0,0))
    screen.blit(croppedProgress, (scale(78,370)))
    imgProgressBarOutlineSurface.blit(imgProgressBarOutlineScaled, (0,0))
    screen.blit(imgProgressBarOutlineScaled, (scale(42,340)))
    button1Surface.blit(imgButtonScaled, (0,0))
    button2Surface.blit(imgButtonScaled, (0,0))
    button3Surface.blit(imgButtonScaled, (0,0))
    button4Surface.blit(imgButtonScaled, (0,0))
    button5Surface.blit(imgButtonScaledSmall, (0,0))
    screen.blit(button1Surface, (scale(430,320)))
    screen.blit(button2Surface, (scale(540,320)))
    screen.blit(button3Surface, (scale(430,400)))
    screen.blit(button4Surface, (scale(540,400)))
    screen.blit(button5Surface, (scale(150,427)))
    screen.blit(enemyScaled, (scale(452, 155)))
    woodenPickaxeSurface.blit(woodenPickaxeScaled, (0,0))
    screen.blit(woodenPickaxeSurface, (scale(100,427)))
    #draw text
    goldText = myfont.render("Gold: {0}".format(int(Materials.gCount)), 1, (0,0,0))
    modifierText = myfont.render("Modifier: {0}".format((1/modifier)), 1, (0,0,0))
    minerText = myfont.render("Miners: {0}".format(miner.num), 1, (0,0,0))
    warriorText = myfont.render("Warriors: {0}".format(warrior.num), 1, (0,0,0))
    woodText = myfont.render("Wood: {0}".format(int(materials.wood)), 1, (0,0,0))
    ironText = myfont.render("Iron: {0}".format(int(materials.iron)), 1, (0,0,0))
    buyMinerText = myfont.render("Buy Miner Gold: {0:6.2f}".format(miner.cost), 1, (0,0,0))
    buyWarriorText = myfont.render("Buy Warrior Gold: {0:6.2f}".format(warrior.cost), 1, (0,0,0))
    emenyHealthText = myfont.render("Enemy Health: {0}".format(enemy.currHealth), 1, (0,0,0))
    mouseXText = myfont.render("X: {0}".format(mouse[0]), 1, (0,0,0))
    mouseYText = myfont.render("Y: {0}".format(mouse[1]), 1, (0,0,0))
    screen.blit(mouseXText, (400, 10))
    screen.blit(mouseYText, (400, 30))
    screen.blit(modifierText, (5, 30))
    screen.blit(emenyHealthText, (200, 30))
    screen.blit(goldText, (5, 10))
    screen.blit(minerText, (5,50))
    screen.blit(woodText, (5, 70))
    screen.blit(ironText, (5, 90))
    screen.blit(buyMinerText, (5, 110))
    screen.blit(buyWarriorText, (250, 110))
    screen.blit(warriorText, (130, 50))
    #display update
    pygame.display.update()
    #clock update
