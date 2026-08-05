import pygame, sys, random
# sys - used to exit the program

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #collision
    #Dont use equals to check for collision, use less than or greater than
    #This is beacause the ball may move more than 1 pixel per frame, so it may skip over the paddle and not register a collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        #reverses the direction of the ball when it hits the top or bottom of the screen
        ball_speed_y *= -1

    #player and opponent score
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        ball_restart()

    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def player_animation():
    #moves the player paddle up and down based on the player_speed variable
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#General setup
#required to initialize pygame
pygame.init()

#runs at a constant speed
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
game_started = False

#Game Rectangles
#the perapeters center the ball in the middle of the screen and make it 30x30
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#text variables
player_score = 0
opponent_score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
message_font = pygame.font.Font("freesansbold.ttf", 24)


# Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

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
                game_started = True
            if event.key == pygame.K_UP:
                player_speed -= 7
                game_started = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    player_animation()

    if game_started:
        ball_animation()
        opponent_ai()

    #visuals
    screen.fill(bg_color)
    
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    #implementing the score
    player_text = font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    #Make the start text appear when the game is not started
    if not game_started:
        start_text = message_font.render("Press UP or DOWN to Start", True, light_grey)
        start_rect = start_text.get_rect(center=(screen_width / 2, 40))
        screen.blit(start_text, start_rect)


    #updating the window
    #drawing the background with whats in the loop
    pygame.display.flip()

    clock.tick(60)