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
                if state != "moving_up":
                    state = "moving_up"
                    pos = [pos[0] + 18, pos[1] - 40]
                    frame = 0
                else:
                    pos = list(pos_tpl)
                    if floor == 0:
                        state = "Idle_ground"
                    elif floor == 1:
                        state = "Idle_1st"
                    elif floor == 2:
                        state = "Idle_2nd"
                    elif floor == 3:
                        state = "Idle_3rd"
                frame = 0
            if event.key == pygame.K_DOWN:
                elevator_speed = 10
                if state != "moving_down":
                    state = "moving_down"
                    pos = [pos[0] + 18, pos[1] + 40]
                    frame = 0
                else:
                    pos = list(pos_tpl)
                    if floor == 0:
                        state = "Idle_ground"
                    elif floor == 1:
                        state = "Idle_1st"
                    elif floor == 2:
                        state = "Idle_2nd"
                    elif floor == 3:
                        state = "Idle_3rd"
                frame = 0                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)

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

    image = StateSystem(state, frame)
    screen.blit(image, pos)

    # print(round(pos[1]))
    current_pos = round(pos[1])

    if state == "moving_up":
        pos[1] -= elevator_speed * dt
        if abs(current_pos - floor_pos_1[1]) < 2:
            in_floor_1 = True
        elif abs(current_pos - floor_pos_2[1]) < 2:
            in_floor_2 = True
        elif abs(current_pos - floor_pos_3[1]) < 2:
            in_floor_3 = True

    elif state == "moving_down":
        pos[1] += elevator_speed * dt
        if abs(current_pos - floor_pos_1[1]) < 2:
            in_floor_1 = True
        elif abs(current_pos - floor_pos_2[1]) < 2:
            in_floor_2 = True
        elif abs(current_pos - floor_pos_3[1]) < 2:
            in_floor_3 = True

    if in_floor_1:
        pos = list(floor_pos_1_tpl)
        state = "Idle_1st"
        floor = 1
        elevator_speed = 0
        in_floor_1 = False

    if in_floor_2:
        pos = list(floor_pos_2_tpl)
        state = "Idle_2nd"
        floor = 2
        elevator_speed = 0
        in_floor_2 = False

    if in_floor_3:
        pos = list(floor_pos_3_tpl)
        state = "Idle_3rd"
        floor = 3
        elevator_speed = 0
        in_floor_3 = False

    if event.type == pygame.KEYDOWN:
        if state == "Idle_1st" and floor == 1 and event.key == pygame.K_UP:
            state = "moving_up"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos - 40]
            frame = 0
        elif state == "Idle_2nd" and floor == 2 and event.key == pygame.K_UP:
            state = "moving_up"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos - 40]
            frame = 0
        elif state == "Idle_3rd" and floor == 3 and event.key == pygame.K_UP:
            state = "moving_up"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos - 40]
            frame = 0
    
        if state == "Idle_1st" and floor == 1 and event.key == pygame.K_DOWN:
            state = "moving_down"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos + 40]
            frame = 0
        elif state == "Idle_2nd" and floor == 2 and event.key == pygame.K_DOWN:
            state = "moving_down"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos + 40]
            frame = 0
        elif state == "Idle_3rd" and floor == 3 and event.key == pygame.K_DOWN:
            state = "moving_down"
            elevator_speed = 10
            pos = [pos[0] + 18, current_pos + 40]
            frame = 0
    pygame.display.update()