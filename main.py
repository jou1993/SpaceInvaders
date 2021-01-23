import  pygame,sys

# Create the screen
screen=pygame.display.set_mode((800,600))

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

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))



#Game Loop
running=True
while running:
    screen.fill(((0,0,0)))
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


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



    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()