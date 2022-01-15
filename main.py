import pygame as pg

pg.init()


# function for events of keyboard
def input_events(event):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
            print("W pressed")


def draw_items():
    global ball_dir
    global ball_dir_y
    global ball_speed

    if score_01 <= 9 or score_02 <= 9:
        screen_game.blit(football_field, (0, 0))
        screen_game.blit(player_01, (50, player_01_y))
        screen_game.blit(player_02, (1140, player_02_y))
        screen_game.blit(ball, (ball_x, ball_y))
        screen_game.blit(score_01_img, (509, 30))
        screen_game.blit(score_02_img, (703, 30))

    if score_01 == 9:
        screen_game.blit(player_01_win, (0, 0))
        ball_speed = 0
        ball_dir = 0
        ball_dir_y = 0
    
    if score_02 == 9:
        screen_game.blit(player_02_win, (0, 0))
        ball_speed = 0
        ball_dir = 0
        ball_dir_y = 0


def movement_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global ball_speed
    global score_01
    global score_02
    global score_01_img
    global score_02_img

    ball_x += ball_speed * ball_dir 
    ball_y += ball_dir_y

    if ball_x < 135:
        if player_01_y < ball_y + 64:
            if player_01_y + 152 > ball_y:
                ball_dir *= -1
                kick_ball.play()

    if ball_x > 1065:
        if player_02_y < ball_y + 64:
            if player_02_y + 152 > ball_y:
                ball_dir *= -1
                kick_ball.play()

    if ball_y > 670:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if score_01 == 5 or score_02 == 5:
        ball_speed = 20

    if ball_x < -90:
        ball_x = 608
        ball_y = 328
        ball_dir_y *= -1
        ball_dir   *= -1
        score_02 += 1
        score_02_img = pg.image.load("assets/sprites/placar/"+str(score_02)+".png")

    if ball_x > 1340:
        ball_x = 608
        ball_y = 328
        ball_dir_y *= -1
        ball_dir   *= -1
        score_01 += 1
        score_01_img = pg.image.load("assets/sprites/placar/"+str(score_01)+".png")

# configs game
SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720
update_game   = True
game_name     = "PONG PYGAME"
clock         = pg.time.Clock()

ball_x      = 608
ball_y      = 328
ball_dir    = -1
ball_dir_y  = 5
ball_speed  = 15
player_01_y = 289
player_02_y = 289

# configs screen game
screen_game = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
title_game  = pg.display.set_caption(game_name)

# musics e sound effects
pg.mixer.music.load("sounds/torcida_sound.wav")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

kick_ball = pg.mixer.Sound("sounds/chute_effect.wav")

# score 
score_01 = 0
score_02 = 0

score_01_img = pg.image.load("assets/sprites/placar/0.png").convert_alpha()
score_02_img = pg.image.load("assets/sprites/placar/0.png").convert_alpha()

# win images
player_01_win = pg.image.load("assets/sprites/hud/player_1_win.png")
player_02_win = pg.image.load("assets/sprites/hud/player_2_win.png")

# image background game
football_field = pg.image.load("assets/sprites/background/field.png").convert()

# players images
player_01 = pg.image.load("assets/sprites/players/player_01.png").convert_alpha()
player_02 = pg.image.load("assets/sprites/players/player_02.png").convert_alpha()

# ball image
ball = pg.image.load("assets/sprites/items/ball.png").convert_alpha()

while update_game:
    clock.tick(60)
    for events in pg.event.get():
        if events.type == pg.QUIT:
            update_game = False
    
    keys = pg.key.get_pressed()

    # movement player 1
    if keys[pg.K_w]:
        player_01_y -= 10
    if keys[pg.K_s]:
        player_01_y += 10

    # moviment player 2
    if keys[pg.K_UP]:
        player_02_y -= 10
    if keys[pg.K_DOWN]:
        player_02_y += 10

    # verification of position
    if player_01_y <= 5:
        player_01_y = 5
    elif player_01_y > 560:
        player_01_y = 562

    if player_02_y <= 5:
        player_02_y = 5
    elif player_02_y > 560:
        player_02_y = 562

    # call the functions here
    draw_items()

    movement_ball()

    pg.display.update()
