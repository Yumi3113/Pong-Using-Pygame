import pygame, sys
# sys - used to exit the program

#General setup
#required to initialize pygame
pygame.init()

clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
#the perapeters center the ball in the middle of the screen and make it 30x30
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
                   
while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #updating the window
    #drawing the background with whats in the loop
    pygame.display.flip()
    
    clock.tick(60)