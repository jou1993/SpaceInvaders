import  pygame,sys
import math
import random
pygame.init()
# Create the screen
screen=pygame.display.set_mode((800,600))

#Background image
backgroundImg=pygame.image.load("3d-space-scene.jpg")

#Set Icon and Title
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load("player.png")
playerX=370
playerY=480
playerX_change=0

#enemy
enemyImg=pygame.image.load("enemy.png")
enemyX=370
enemyY=50
enemyX_change=0.3
enemyY_change=40

#bullet 
bulletImg=pygame.image.load("bullet.png")
bulletX=370
bulletY=480
bulletX_change=0
bulletY_change=1
bullet_state= "ready"

#score
score_value=0
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    return distance < 30

#Game Loop
running=True
while running:
    screen.fill(((0,0,0)))
    #background image
    screen.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        #if X is pressed
        if event.type == pygame.QUIT:
            running=False
        #if any key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Collision
    collision=isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY=480
        bullet_state="ready"
        score_value += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
    #enemy movement
    enemyX += enemyX_change

    if enemyX <=0 :
        enemyX=0
        enemyX_change =0.3
        enemyY += enemyY_change
    if enemyX >= 736 :
        enemyX=736
        enemyX_change = -0.3
        enemyY += enemyY_change


    #Check Boundaries
    if playerX <=0 :
        playerX=0
    if playerX >= 736 :
        playerX=736

    #change the position of the player
    playerX += playerX_change

    #bullet movement
    if bulletY <=0 :
        bulletY=480
        bullet_state="ready"
    if bullet_state== "fire"  :
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()