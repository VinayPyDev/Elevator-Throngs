import pygame
from art import RenderElevatorIdle1st, RenderElevatorIdle2nd, RenderElevatorIdle3rd, RenderElevatorIdleGround
from display import RenderElevatorUp, RenderElevatorDown

sprites = {}

sprites.update(RenderElevatorIdleGround())
sprites.update(RenderElevatorIdle1st())
sprites.update(RenderElevatorIdle2nd())
sprites.update(RenderElevatorIdle3rd())

sprites["moving_up"] = RenderElevatorUp()
sprites["moving_down"] = RenderElevatorDown()

sprite = "Idle_ground"

def StateSystem(state, frame_index):
    global sprites

    current = sprites[state]

    if isinstance(current, list):
        image = current[int(frame_index) % len(current)]
    else:
        image = current

    return image