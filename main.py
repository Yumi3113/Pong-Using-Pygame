import pygame, sys
# sys - used to exit the program

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #collision
    #Dont use equals to check for collision, use less than or greater than
    #This is beacause the ball may move more than 1 pixel per frame, so it may skip over the paddle and not register a collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        #reverses the direction of the ball when it hits the top or bottom of the screen
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        #reverses the direction of the ball when it hits the player or opponent paddle
        ball_speed_x *= -1


def player_animation():
    #moves the player paddle up and down based on the player_speed variable
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


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

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #handing key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()

    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    #updating the window
    #drawing the background with whats in the loop
    pygame.display.flip()
    
    clock.tick(60)