import pygame
import sys

from state import StateSystem, sprites

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elevator Throngs")
clock = pygame.time.Clock()

# -------------------
# BASIC SETUP
# -------------------
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 200

idle_x = 560
moving_x = 560 + 18

state = "Idle_ground"

# TRUE POSITION (LOGIC)
pos = [idle_x, 580]

# FLOORS (PURE Y VALUES)
floors = {
    0: 580,
    1: 450,
    2: 350,
    3: 250
}

floor = 0

elevator_speed = 200  # pixels/sec (cleaner than your dt * 10)

# -------------------
# MAIN LOOP
# -------------------
while True:
    dt = clock.tick(60) / 1000
    screen.fill((0, 0, 0))

    # -------------------
    # INPUT
    # -------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if state.startswith("Idle") and floor < 3:
                    state = "moving_up"
                    pos[0] = moving_x

            if event.key == pygame.K_DOWN:
                if state.startswith("Idle") and floor > 0:
                    state = "moving_down"
                    pos[0] = moving_x

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # -------------------
    # ANIMATION
    # -------------------
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

    # -------------------
    # MOVEMENT
    # -------------------
    prev_y = pos[1]

    if state == "moving_up":
        pos[1] -= elevator_speed * dt

        # Check if crossed next floor
        target_floor = floor + 1
        if target_floor in floors:
            target_y = floors[target_floor]

            if prev_y > target_y >= pos[1]:
                pos[1] = target_y
                floor = target_floor
                state = f"Idle_{['ground','1st','2nd','3rd'][floor]}"
                pos[0] = idle_x

    elif state == "moving_down":
        pos[1] += elevator_speed * dt

        target_floor = floor - 1
        if target_floor in floors:
            target_y = floors[target_floor]

            if prev_y < target_y <= pos[1]:
                pos[1] = target_y
                floor = target_floor
                state = f"Idle_{['ground','1st','2nd','3rd'][floor]}"
                pos[0] = idle_x

    # -------------------
    # VISUAL OFFSET (ONLY RENDERING)
    # -------------------
    offset_y = 0

    if state == "moving_up":
        offset_y = -40
    elif state == "moving_down":
        offset_y = 0

    # -------------------
    # DRAW
    # -------------------
    screen.blit(image, (pos[0], pos[1] + offset_y))

    pygame.display.update()