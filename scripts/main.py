import pygame
import sys

from display import RenderElevatorUp
from state import StateSystem, sprites

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elevator Throngs")
clock = pygame.time.Clock()
dt = 0

frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 200

idle_x = 560
moving_x = 560 + 18

x_18 = 18

state = "Idle_ground"
pos_tpl = (560, 580)
pos = list(pos_tpl)

floor_pos_1_tpl = (560, 450)
floor_pos_2_tpl = (560, 350)
floor_pos_3_tpl = (560, 250)

floor_pos_1 = list(floor_pos_1_tpl)
floor_pos_2 = list(floor_pos_2_tpl)
floor_pos_3 = list(floor_pos_3_tpl)

floor = 0
in_floor_1 = False
in_floor_2 = False
in_floor_3 = False

floor_moving_up_1 = floor_pos_1[1] - 40
floor_moving_up_2 = floor_pos_2[1] - 40
floor_moving_up_3 = floor_pos_3[1] - 40

floor_moving_down_1 = floor_pos_1[1]
floor_moving_down_2 = floor_pos_2[1]
floor_moving_down_3 = floor_pos_3[1]

floor_moving_down_0 = pos[1]

elevator_speed = 10

while True:
    dt = clock.tick(60) / 1000

    mouse_pos = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                elevator_speed = 10
                if state != "moving_up" and state in ("Idle_ground", "Idle_1st", "Idle_2nd"):
                    state = "moving_up"
                    pos = [moving_x, pos[1] - 40]
                    frame = 0
                frame = 0
            if event.key == pygame.K_DOWN:
                elevator_speed = 10
                if state != "moving_down" and state in ("Idle_ground", "Idle_1st", "Idle_2nd", "Idle_3rd"):
                    state = "moving_down"
                    pos = [idle_x + x_18, pos[1]]
                    frame = 0
                frame = 0
                   
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    current = sprites[state]

    if isinstance(current, list):
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            last_update = current_time
            frame += 1

            if frame >= len(current):
                frame = 0
    else:
        frame = 0

    # print(round(pos[1]))

    current_pos = pos[1]

    if state == "moving_up":
        pos[1] -= elevator_speed * dt * 10
        current_pos = pos[1] 
        if abs(current_pos - floor_moving_up_1) < 1.6 and floor < 1:
            in_floor_1 = True
        elif abs(current_pos - floor_moving_up_2) < 1.6 and floor < 2:
            in_floor_2 = True
        elif abs(current_pos - floor_moving_up_3) < 1.6 and floor < 3:
            in_floor_3 = True

    elif state == "moving_down":
        pos[1] += elevator_speed * dt * 10
        current_pos = pos[1] + 40
        if abs(current_pos - floor_moving_down_1) < 1.6 and floor >= 1:
            in_floor_1 = True
        elif abs(current_pos - floor_moving_down_2) < 1.6 and floor >= 2:
            in_floor_2 = True
        elif abs(current_pos - floor_moving_down_3) < 1.6 and floor >= 3:
            in_floor_3 = True

    if state == "moving_down" and pos[1] + 40 >= pos_tpl[1]:
        pos = [idle_x, pos_tpl[1]]
        state = "Idle_ground"
        floor = 0
        frame = 0
        elevator_speed = 0

    if in_floor_1:
        pos = [idle_x, floor_pos_1_tpl[1]]
        state = "Idle_1st"
        floor = 1
        elevator_speed = 0
        in_floor_1 = False

    if in_floor_2:
        pos = [idle_x, floor_pos_2_tpl[1]]
        state = "Idle_2nd"
        floor = 2
        elevator_speed = 0
        in_floor_2 = False

    if in_floor_3:
        pos = [idle_x, floor_pos_3_tpl[1]]
        state = "Idle_3rd"
        floor = 3
        elevator_speed = 0
        in_floor_3 = False

    image = StateSystem(state, frame)
    screen.blit(image, pos)    
    pygame.display.update()