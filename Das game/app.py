import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((400,250))
pygame.display.set_caption('Das Game')

#initiations
clock=pygame.time.Clock()
player=game_objects.Player(0,0)
#set random spawn
player.x=random.randint(player.size, player.width)
player.y=random.randint(player.size, player.height)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)
    player.update()
    DISPLAYSURF.fill((255, 255, 255))
    player.draw(DISPLAYSURF)
    
    player.move("x")
    player.move("y")
    
    #when player hits border
    if(player.x > player.width-player.size or player.x < 0+player.size):
        player.flipDir("x")
        player.color_shift("true")
        player.border_hit(DISPLAYSURF)
    #when player hits border
    if(player.y > player.height-player.size or player.y < 0+player.size):
        player.flipDir("y")
        player.color_shift("true")
        player.border_hit(DISPLAYSURF)
    
    print("x:", player.x, "  y:", player.y)