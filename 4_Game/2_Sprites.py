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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0,0))
    screen.blit(char, (char_x, char_y))

    pygame.display.update()

pygame.quit()