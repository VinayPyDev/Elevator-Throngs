import pygame
import sys
import random

# State system import
from state import StateSystem, sprites

# Asset imports
from art import Buttons, FloorMarkers, SourceBoard, ElectricityMeter, WeightMeter, RepairMeter, ElevatorLine
from display import RenderButtonFloor0, RenderButtonFloor1, RenderButtonFloor2, RenderButtonFloor3, RenderButtonMovingDown, RenderButtonMovingDown1, RenderButtonMovingDown2, RenderButtonMovingDown3
from display import RenderButtonMovingUp, RenderButtonMovingUp1, RenderButtonMovingUp2, RenderButtonMovingUp3, RenderFloor0Marker, RenderFloor1Marker, RenderFloor2Marker, RenderFloor3Marker
from display import RenderSourceBoard, RenderElevatorLine

# Electricity import from display
from display import RenderNoElectricity, Render1Electricity, Render2Electricity, Render3Electricity, Render4Electricity, Render5Electricity
# Wt import from display
from display import Render150Weight, Render250Weight, Render300Weight, Render350Weight, Render400Weight
# Repair import from display
from display import Render0Repair, Render1Repair, Render2Repair, Render3Repair, Render4Repair, Render5Repair

# Worker imgs and animations
from entity import worker_frames, brown_worker_frames, grey_worker_frames
import entity

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elevator Throngs")
clock = pygame.time.Clock()
dt = 0

art = {}

art.update(Buttons())
art.update(FloorMarkers())
art.update(SourceBoard())

art.update(ElectricityMeter())
art.update(WeightMeter())
art.update(RepairMeter())

art.update(ElevatorLine())

# workers pos
worker_move_timer = random.uniform(1.5, 4.0)
worker_pos = [
    # [at floor 0]
    [random.randint(12, 1275), 580], [random.randint(60, 875), 580], [random.randint(34, 972), 580]
]
worker_state = "moving"
is_worker_moving = True

electricity = 3
weight = 150
repair = 3

frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 200

idle_x = 560
moving_x = 560 + 18

x_18 = 18

state = "Idle_ground"
pos_tpl = (560, 580)
pos = list(pos_tpl)

floor_pos_1_tpl = (560, 480)
floor_pos_2_tpl = (560, 380)
floor_pos_3_tpl = (560, 280)

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

elevator_speed = 10

electricity_charge_timer = 3

moving_down_trigger = False

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
                if state != "moving_down" and state in ("Idle_1st", "Idle_2nd", "Idle_3rd"):
                    state = "moving_down"
                    pos = [idle_x + x_18, pos[1]]
                    moving_down_trigger = True
                    frame = 0
                frame = 0
            if state == "moving_down":
                if moving_down_trigger:
                    pos[1] -= 40
                    moving_down_trigger = False
                   
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    worker_move_timer -= dt
    if worker_move_timer <= 0:
        is_worker_moving = not is_worker_moving

        if is_worker_moving:
            worker_move_timer = random.uniform(2, 5)
        else:
            worker_move_timer = random.uniform(0.5, 2)

    if is_worker_moving:
        for worker in worker_pos:
            worker[0] += 23 * dt
            # worker[1] += 34 * dt
            # worker[2] -= 53 * dt

            if worker[0] >= 1280:
                worker[0] -= 23 * dt
            elif worker[0] <= 0:
                worker[0] += 23 * dt

            # if worker[1] >= 1280:
            #     worker[1] -= 34 * dt
            # elif worker[1] <= 0:
            #     worker[1] += 34 * dt

            # # if worker[2] >= 1280:
            # #     worker[2] -= 53 * dt
            # # elif worker[2] <= 0:
            # #     worker[2] += 53 * dt

    entity.anim_timer += dt * 1000
    if entity.anim_timer >= entity.frame_duration:
        entity.current_frame = (entity.current_frame + 1) % len(worker_frames)
        entity.anim_timer = 0

    RenderElevatorLine(screen, art)

    RenderButtonFloor0(screen, art)
    RenderButtonFloor1(screen, art)
    RenderButtonFloor2(screen, art)
    RenderButtonFloor3(screen, art)

    if state == "moving_up":
        if floor == 0:
            RenderButtonMovingUp(screen, art)
        elif floor == 1:
            RenderButtonMovingUp1(screen, art)
        elif floor == 2:
            RenderButtonMovingUp2(screen, art)
        elif floor == 3:
            RenderButtonMovingUp3(screen, art)
    if state == "moving_down":
        if floor == 0:
            RenderButtonMovingDown(screen, art)
        elif floor == 1:
            RenderButtonMovingDown1(screen, art)
        elif floor == 2:
            RenderButtonMovingDown2(screen, art)
        elif floor == 3:
            RenderButtonMovingDown3(screen, art)

    if floor == 0:
        RenderFloor0Marker(screen, art)
    elif floor == 1:
        RenderFloor1Marker(screen, art)
    elif floor == 2:
        RenderFloor2Marker(screen, art)
    elif floor == 3:
        RenderFloor3Marker(screen, art)

    RenderSourceBoard(screen, art)

    if electricity == 0:
        RenderNoElectricity(screen, art)
    elif electricity == 1:
        Render1Electricity(screen, art)
    elif electricity == 2:
        Render2Electricity(screen, art)
    elif electricity == 3:
        Render3Electricity(screen, art)
    elif electricity == 4:
        Render4Electricity(screen, art)
    elif electricity == 5:
        Render5Electricity(screen, art)

    if weight == 150:
        Render150Weight(screen, art)
    elif weight == 250:
        Render250Weight(screen, art)
    elif weight == 300:
        Render300Weight(screen, art)
    elif weight == 350:
        Render350Weight(screen, art)
    elif weight == 400:
        Render400Weight(screen, art)

    if repair == 0:
        Render0Repair(screen, art)
    elif repair == 1:
        Render1Repair(screen, art)
    elif repair == 2:
        Render2Repair(screen, art)
    elif repair == 3:
        Render3Repair(screen, art)
    elif repair == 4:
        Render4Repair(screen, art)
    elif repair == 5:
        Render5Repair(screen, art)
    
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

    if is_worker_moving:
        for x, y in worker_pos:
            screen.blit(worker_frames[entity.current_frame], (x, y))
            screen.blit(brown_worker_frames[entity.current_frame], (x, y))
            screen.blit(grey_worker_frames[entity.current_frame], (x, y))

    image = StateSystem(state, frame)
    screen.blit(image, pos)    

    pygame.display.update()