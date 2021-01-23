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

def player(x,y):
    screen.blit(playerImg,(x,y))




#Game Loop
running=True
while running:
    screen.fill(((0,0,0)))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False

        player(playerX,playerY)
        pygame.display.update()