import  pygame,sys

# Create the screen
screen=pygame.display.set_mode((800,600))

#Set Icon and Title
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)





#Game Loop
running=True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False