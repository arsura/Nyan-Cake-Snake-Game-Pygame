import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
orange = (243, 176, 17)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("Contents/snake_head 2.png")
pygame.display.set_icon(icon)

snake_img = pygame.image.load("Contents/snake_head.png")
speed_up_img = pygame.image.load("Contents/speed_up.png")
snake_body_img = pygame.image.load("Contents/snake_body.png")
start_screen_img = pygame.image.load("Contents/start_screen.png")
apple_img = pygame.image.load("Contents/apple_food.png")
poison_img = pygame.image.load("Contents/poison.png")
health_img = pygame.image.load("Contents/health.png")
wall_img = pygame.image.load("Contents/wall.png")
wall_img2 = pygame.image.load("Contents/wall_2.png")
fire_img = pygame.image.load("Contents/fire.png")
game_over_img = pygame.image.load("Contents/game_over.png")



pygame.display.update()

clock = pygame.time.Clock()

apple_thickness = 30
block_size = 20

small_font = pygame.font.SysFont("Lucida Console", 20)
med_font = pygame.font.SysFont("Lucida Console", 30)
large_font = pygame.font.SysFont("Lucida Console", 50)

def pause():

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


        #game_display.fill(orange)
        #screen_message("Pause", white, -100, size="large")
        #screen_message("Press Spacebar to play again or Esc to quit", black, -50, size="medium")
        pause_screen_img = pygame.image.load("Contents/pause.png")
        game_display.blit(pause_screen_img, (0, 0))
        pygame.display.update()
        clock.tick(5)

def score(score):
    score_text = small_font.render("Score: "+str(score), True, white)
    game_display.blit(score_text, [30, 30])

def life(life):

    life_text = small_font.render("Life: "+str(life), True, white)
    game_display.blit(life_text, [30, 60])

def random_apple():

    apple_x = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    apple_y = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    apple_x2 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    apple_y2 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    apple_x3 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    apple_y3 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    apple_x4 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    apple_y4 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    return apple_x, apple_y

def random_poison():

    poison_x = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    poison_y = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    poison_x2 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    poison_y2 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    poison_x3 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    poison_y3 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    poison_x4 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    poison_y4 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    poison_x5 = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    poison_y5 = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    return poison_x, poison_y

def fire_ball():

    fire_x = 0
    fire_y = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    return fire_x, fire_y

def random_health():

    health_x = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    health_y = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    return health_x, health_y

def random_speed_up():

    speed_up_x = round(random.randrange(20, display_width - apple_thickness - 20))#/10.0)*10.0
    speed_up_y = round(random.randrange(20, display_height - apple_thickness - 20))#/10.0)*10.0
    return speed_up_x, speed_up_y

def wall_left():

    wall_x_left = 0#round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
    wall_y_left = 0#round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0

    return wall_x_left, wall_y_left

def wall_right():

    wall_x_right = 780#round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
    wall_y_right = 0#round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0

    return wall_x_right, wall_y_right

def wall_up():

    wall_x_up = 0#round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
    wall_y_up = 0#round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0

    return wall_x_up, wall_y_up

def wall_down():

    wall_x_down = 0#round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
    wall_y_down = 580#round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0

    return wall_x_down, wall_y_down

def game_intro_screen():

    intro = True
    while intro:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == 13:
                    intro = False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


        game_display.fill(orange)
        #screen_message("Welcome to Snake Game !!", white, displace_y=-100, size="large")
        #screen_message("Midtrem Project Computer Engineering Naresuan Uviversity", black, displace_y=-50, size="small")
        game_display.blit(start_screen_img, (0, 0))
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(snake_img, 270)
        body = pygame.transform.rotate(snake_body_img, 270)
    if direction == "left":
        head = pygame.transform.rotate(snake_img, 90)
        body = pygame.transform.rotate(snake_body_img, 90)
    if direction == "up":
        head = snake_img
        body = snake_body_img
    if direction == "down":
        head = pygame.transform.rotate(snake_img, 180)
        body = pygame.transform.rotate(snake_body_img, 180)

    game_display.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for x_and_y in snakelist[:-1]:
        #pygame.draw.rect(game_display, black, [x_and_y[0], x_and_y[1], block_size, block_size])
        game_display.blit(body, [x_and_y[0], x_and_y[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = med_font.render(text, True, color)
    if size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def screen_message(msg, color, displace_y=0 , size = "small"):
    #screen_text = font.render(msg, True, color)
    #game_display.blit(screen_text, [180, display_height/2])
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2), (display_height/2) + displace_y
    game_display.blit(text_surf, text_rect)

def game_loop():

    global direction
    direction = "right"

    game_exit = False
    game_over = False

    position_x = display_width/2
    position_y = display_height/2

    change_position_x = 0
    change_position_y = 0

    FPS = 15
    life_count = 0

    snake_list = []
    snake_length = 1

    apple_x, apple_y = random_apple()
    apple_x2, apple_y2 = random_apple()
    apple_x3, apple_y3 = random_apple()
    apple_x4, apple_y4 = random_apple()

    poison_x, poison_y = random_poison()
    poison_x2, poison_y2 = random_poison()
    poison_x3, poison_y3 = random_poison()
    poison_x4, poison_y4 = random_poison()
    poison_x5, poison_y5 = random_poison()

    health_x, health_y = random_health()

    wall_x_left, wall_y_left = wall_left()
    wall_x_right, wall_y_right = wall_right()
    wall_x_up, wall_y_up = wall_up()
    wall_x_down, wall_y_down = wall_down()

    speed_up_x, speed_up_y = random_speed_up()
    fire_x, fire_y = fire_ball()

    while not game_exit:

        while game_over == True:

            #game_display.fill(white)
            #screen_message("Game over", black, displace_y=-50, size="large")
            #screen_message("Press Spacebar to play again or Esc to quit", orange, size="medium")
            game_display.blit(game_over_img, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and change_position_x != +block_size:
                    direction = "left"
                    change_position_x = -block_size
                    change_position_y = 0

                elif event.key == pygame.K_RIGHT and change_position_x != -block_size:
                    direction = "right"
                    change_position_x = block_size
                    change_position_y = 0


                elif event.key == pygame.K_UP and change_position_y != +block_size:
                    direction = "up"
                    change_position_y = -block_size
                    change_position_x = 0

                elif event.key == pygame.K_DOWN  and change_position_y != -block_size:
                    direction = "down"
                    change_position_y = block_size
                    change_position_x = 0



## Speed x2 ## ____________________________________________________________________________________________________

                elif event.key == pygame.K_a and change_position_x != +block_size*2:
                    direction = "left"
                    change_position_x = -block_size*2
                    change_position_y = 0

                elif event.key == pygame.K_d and change_position_x != -block_size*2:
                    direction = "right"
                    change_position_x = block_size*2
                    change_position_y = 0

                elif event.key == pygame.K_w and change_position_y != +block_size*2:
                    direction = "up"
                    change_position_y = -block_size*2
                    change_position_x = 0

                elif event.key == pygame.K_s and change_position_y != -block_size*2:
                    direction = "down"
                    change_position_y = block_size*2
                    change_position_x = 0

                elif event.key == pygame.K_p:
                    pause()
## ____________________________________________________________________________________________________

                elif event.key == pygame.K_ESCAPE:
                    game_exit = True
                    game_over = False

                elif event.key == pygame.K_SPACE:
                    game_loop()

                elif event.key == pygame.K_BACKSPACE:
                    game_intro_screen()

                elif event.key == pygame.K_b:
                    FPS = 15

        #    if event.type == pygame.KEYUP:
        #        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #            change_position_x = 0
        #        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #            change_position_y = 0
        #if position_x >= display_width or position_x < 0 or position_y >= display_height or position_y < 0:

        if position_x >= display_width-20 or position_x <= 0 or position_y >= display_height-20 or position_y <= 20:
            life_count += 1
            change_position_y = 0
            change_position_x = 1
            position_x = 400
            position_y = 300


        print(life_count)

        fire_x += 10
        if fire_x == 800:
            fire_x = 0
            if fire_x == 0:
                fire_x += 10
#
        position_x += change_position_x
        position_y += change_position_y

        #game_display.fill(black)
        screen_game_img = pygame.image.load("Contents/screen_game.png")
        game_display.blit(screen_game_img, (0, 0))

        game_display.blit(apple_img, (apple_x, apple_y))
        game_display.blit(apple_img, (apple_x2, apple_y2))
        game_display.blit(apple_img, (apple_x3, apple_y3))
        game_display.blit(apple_img, (apple_x4, apple_y4))

        game_display.blit(poison_img, (poison_x, poison_y))
        game_display.blit(poison_img, (poison_x2, poison_y2))
        game_display.blit(poison_img, (poison_x3, poison_y3))
        game_display.blit(poison_img, (poison_x4, poison_y4))
        game_display.blit(poison_img, (poison_x5, poison_y5))

        game_display.blit(health_img, (health_x, health_y))

        game_display.blit(wall_img, (wall_x_left, wall_y_left))
        game_display.blit(wall_img, (wall_x_right, wall_y_right))
        game_display.blit(wall_img2, (wall_x_up, wall_y_up))
        game_display.blit(wall_img2, (wall_x_down, wall_y_down))

        game_display.blit(speed_up_img, (speed_up_x, speed_up_y))
        game_display.blit(fire_img, (fire_x, fire_y))


        snake_head = []
        snake_head.append(position_x)
        snake_head.append(position_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                life_count += 1
                change_position_y = 0
                change_position_x = 1
                position_x = 400
                position_y = 300
                #game_over = True

        #if snake_length == 0:
        #game_over = True
        snake(block_size, snake_list)
        score(snake_length-1)
        life(5-life_count)
        pygame.display.update()

#        if position_x == apple_x and position_y == apple_y:
#            apple_x = round(random.randrange(0, display_width - apple_thickness)/10.0)*10.0
#            apple_y = round(random.randrange(0, display_height - apple_thickness)/10.0)*10.0
#            snake_length += 1

#        if position_x >= apple_x and position_x <= apple_x + apple_thickness:
#            if position_y >= apple_y and position_y <= apple_y + apple_thickness:
#                apple_x = round(random.randrange(0, display_width - apple_thickness))#/10.0)*10.0
#                apple_y = round(random.randrange(0, display_height - apple_thickness))#/10.0)*10.0
#                snake_length += 1

#Apple 1

        if position_x > apple_x and position_x < apple_x + apple_thickness or position_x + block_size > apple_x and position_x + block_size < apple_x + apple_thickness:
            if position_y > apple_y and position_y < apple_y + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x, apple_y = random_apple()
                snake_length += 1


            elif position_y + block_size > apple_y and position_y + block_size < apple_y + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x, apple_y = random_apple()
                snake_length += 1

#Apple 2

        if position_x > apple_x2 and position_x < apple_x2 + apple_thickness or position_x + block_size > apple_x2 and position_x + block_size < apple_x2 + apple_thickness:
            if position_y > apple_y2 and position_y < apple_y2 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x2, apple_y2 = random_apple()
                snake_length += 1


            elif position_y + block_size > apple_y2 and position_y + block_size < apple_y2 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x2, apple_y2 = random_apple()
                snake_length += 1

#Apple 3

        if position_x > apple_x3 and position_x < apple_x3 + apple_thickness or position_x + block_size > apple_x3 and position_x + block_size < apple_x3 + apple_thickness:
            if position_y > apple_y3 and position_y < apple_y3 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x3, apple_y3 = random_apple()
                snake_length += 1


            elif position_y + block_size > apple_y3 and position_y + block_size < apple_y3 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x3, apple_y3 = random_apple()
                snake_length += 1

#Apple 4

        if position_x > apple_x4 and position_x < apple_x4 + apple_thickness or position_x + block_size > apple_x4 and position_x + block_size < apple_x4 + apple_thickness:
            if position_y > apple_y4 and position_y < apple_y4 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x4, apple_y4 = random_apple()
                snake_length += 1


            elif position_y + block_size > apple_y4 and position_y + block_size < apple_y4 + apple_thickness:

                fire_x, fire_y = fire_ball()
                apple_x4, apple_y4 = random_apple()
                snake_length += 1


#Poison 1

        if position_x > poison_x and position_x < poison_x + apple_thickness or position_x + block_size > poison_x and position_x + block_size < poison_x + apple_thickness:
            if position_y > poison_y and position_y < poison_y + apple_thickness:

                poison_x, poison_y = random_poison()
                FPS = 3

            elif position_y + block_size > poison_y and position_y + block_size < poison_y + apple_thickness:

                poison_x, poison_y = random_poison()
                FPS = 3

#Poison 2

        if position_x > poison_x2 and position_x < poison_x2 + apple_thickness or position_x + block_size > poison_x2 and position_x + block_size < poison_x2 + apple_thickness:
            if position_y > poison_y2 and position_y < poison_y2 + apple_thickness:

                poison_x2, poison_y2 = random_poison()
                FPS = 3

            elif position_y + block_size > poison_y2 and position_y + block_size < poison_y2 + apple_thickness:

                poison_x2, poison_y2 = random_poison()
                FPS = 3

#Poison 3

        if position_x > poison_x3 and position_x < poison_x3 + apple_thickness or position_x + block_size > poison_x3 and position_x + block_size < poison_x3 + apple_thickness:
            if position_y > poison_y3 and position_y < poison_y3 + apple_thickness:

                poison_x3, poison_y3 = random_poison()
                FPS = 3

            elif position_y + block_size > poison_y2 and position_y + block_size < poison_y2 + apple_thickness:

                poison_x3, poison_y3 = random_poison()
                FPS = 3

#Poison 4

        if position_x > poison_x4 and position_x < poison_x4 + apple_thickness or position_x + block_size > poison_x4 and position_x + block_size < poison_x4 + apple_thickness:
            if position_y > poison_y4 and position_y < poison_y4 + apple_thickness:

                poison_x4, poison_y4 = random_poison()
                FPS = 3

            elif position_y + block_size > poison_y4 and position_y + block_size < poison_y4 + apple_thickness:

                poison_x4, poison_y4 = random_poison()
                FPS = 3

#Poison 5

        if position_x > poison_x5 and position_x < poison_x5 + apple_thickness or position_x + block_size > poison_x5 and position_x + block_size < poison_x5 + apple_thickness:
            if position_y > poison_y5 and position_y < poison_y5 + apple_thickness:

                poison_x5, poison_y5 = random_poison()
                FPS = 3

            elif position_y + block_size > poison_y5 and position_y + block_size < poison_y5 + apple_thickness:

                poison_x5, poison_y5 = random_poison()
                FPS = 3

#Health 1

        if position_x > health_x and position_x < health_x + apple_thickness or position_x + block_size > health_x and position_x + block_size < health_x + apple_thickness:
            if position_y > health_y and position_y < health_y + apple_thickness:

                health_x, health_y = random_health()
                FPS = 15

            elif position_y + block_size > health_y and position_y + block_size < health_y + apple_thickness:

                health_x, health_y = random_health()
                FPS = 15


#The Flash 1

        if position_x > speed_up_x and position_x < speed_up_x + apple_thickness or position_x + block_size > speed_up_x and position_x + block_size < speed_up_x + apple_thickness:
            if position_y > speed_up_y and position_y < speed_up_y + apple_thickness:

                speed_up_x, speed_up_y = random_speed_up()
                FPS = 30


            elif position_y + block_size > speed_up_y and position_y + block_size < speed_up_y + apple_thickness:

                speed_up_x, speed_up_y = random_speed_up()
                FPS = 30


#Fire 1

        if position_x > fire_x and position_x < fire_x + apple_thickness or position_x + block_size > fire_x and position_x + block_size < fire_x + apple_thickness:
            if position_y > fire_y and position_y < fire_y + apple_thickness:

                position_x = 400
                position_y = 300
                change_position_y = 0
                change_position_x = 1
                life_count += 1

            elif position_y + block_size > fire_y and position_y + block_size < fire_y + apple_thickness:

                position_x = 400
                position_y = 300
                change_position_y = 0
                change_position_x = 1
                life_count += 1


        if life_count == 5:
            game_over = True

        clock.tick(FPS)



    pygame.quit()
    quit()



game_intro_screen()
game_loop()
