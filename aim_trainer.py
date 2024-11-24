import pygame
from random import randint

def display_points(points):
    score_surf = point_font.render(f"{points}", False, "Black")
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

def position_target():
    target_x_pos = randint(55, 745)
    target_y_pos = randint(55, 345)
    target_rect = target_surf.get_rect(center = (target_x_pos, target_y_pos))     
    return target_rect

pygame.init()

pygame.display.set_caption("Aim Trainner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# MUSIC
ding = pygame.mixer.Sound("audio/ding.wav")
ding.set_volume(0.05)

# TARGET
target_surf = pygame.image.load("graphics/target.png").convert_alpha()
# target_surf.fill("#6bd68b")
target_x_pos = randint(55, 745)
target_y_pos = randint(55, 345)
target_rect = target_surf.get_rect(center = (target_x_pos, target_y_pos))

# Title:
point_font = pygame.font.Font("font/Pixeltype.ttf", 80)
title_font = pygame.font.Font("font/Pixeltype.ttf", 120)
title_surf = title_font.render("AIM TRAINER", False, "Black")
title_rect = title_surf.get_rect(center = (400, 70))

# Click to start
message_font = pygame.font.Font("font/Pixeltype.ttf", 50)
score_font = pygame.font.Font("font/Pixeltype.ttf", 35)
click_to_start = message_font.render("click to start", False, "Black")
click_to_start_rect = click_to_start.get_rect(center = (400, 115))

# Start Target:
start_button = pygame.transform.rotozoom(target_surf, 0, 1.5)
start_button_rect = start_button.get_rect(center = (400, 225))

# GAME PROPERTIES
points = 30
game_active = False
start_time = 0
click_time_list = []

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if target_rect.collidepoint(pygame.mouse.get_pos()):
                    points -= 1
                    target_rect = position_target()
                    click_time_list.append(click_time)
                    start_time = pygame.time.get_ticks()
                    ding.play()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game_active = True
                    click_time_list.clear()
                    ding.play()

    screen.fill("#d6d6d6")

    if game_active:
        click_time = pygame.time.get_ticks() - start_time
        if points <= 0:
            game_active = False
            points = 30
        else:
            display_points(points)
            screen.blit(target_surf, target_rect)

    else:
        screen.blit(title_surf, title_rect)
        screen.blit(click_to_start, click_to_start_rect)
        screen.blit(start_button, start_button_rect)
        if click_time_list:
            average_time = sum(click_time_list) // len(click_time_list)
            score_message = score_font.render(f"average time per target: {average_time}ms", False, "Black")
            score_message_rect = score_message.get_rect(center = (400, 350))
            screen.blit(score_message, score_message_rect)


    pygame.display.update()
    clock.tick(60)
