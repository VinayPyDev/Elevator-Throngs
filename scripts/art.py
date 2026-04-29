import pygame
import os
import sys

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def RenderElevatorIdleGround():
    return {
        "Idle_ground": pygame.transform.scale(pygame.image.load(resource_path("data/Sprite-0001.png")).convert_alpha(), (64 * 2, 64 * 2))
    }

def RenderElevatorIdle1st():
    return {
        "Idle_1st": pygame.transform.scale(pygame.image.load(resource_path("data/Sprite-0001_2.png")).convert_alpha(), (64 * 2, 64 * 2))
    }

def RenderElevatorIdle2nd():
    return {
        "Idle_2nd": pygame.transform.scale(pygame.image.load(resource_path("data/Sprite-0001_3.png")).convert_alpha(), (64 * 2, 64 * 2))
    }

def RenderElevatorIdle3rd():
    return {
        "Idle_3rd": pygame.transform.scale(pygame.image.load(resource_path("data/Sprite-0001_4.png")).convert_alpha(), (64 * 2, 64 * 2))
    }
