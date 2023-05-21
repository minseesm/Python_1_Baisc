import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load("4_Game/images/background.png")

pygame.display.set_caption("MINEW - Shooting game")

# Character
char = pygame.image.load("4_Game/images/P_character.png")
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x = screen_width/2 - char_width/2
char_y = screen_height/2 - char_height/2

char_x_to = 0
char_y_to = 0

char_speed = 0.6

clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)
total_time = 10
start_ticks = pygame.time.get_ticks()

running = True
while running:
    frame = clock.tick(100)      # 60~120

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                char_y_to -= char_speed
            elif event.key == pygame.K_DOWN:
                char_y_to += char_speed
            elif event.key == pygame.K_LEFT:
                char_x_to -= char_speed
            elif event.key == pygame.K_RIGHT:
                char_x_to += char_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                char_y_to = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_x_to = 0

    # Charater move
    char_x += char_x_to * frame
    char_y += char_y_to * frame

    if char_x < 0:
        char_x = 0
    elif char_x > screen_width - char_width:
        char_x = screen_width - char_width

    if char_y < 0:
        char_y = 0
    elif char_y > screen_height - char_height:
        char_y = screen_height - char_height
    
    screen.blit(background, (0,0))
    screen.blit(char, (char_x, char_y))

    past_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(round((total_time - past_time),2)), True, (255, 255, 255))

    screen.blit(timer, (10,10))

    if total_time - past_time < 0 :
        running = False

    pygame.display.update()

pygame.quit()