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

# Buttons
def Buttons():
    return {
        "button1": pygame.image.load(resource_path("data/button1.png")).convert_alpha(),
        "button2": pygame.image.load(resource_path("data/button2.png")).convert_alpha(),
        "button3": pygame.image.load(resource_path("data/button3.png")).convert_alpha()
    }

def FloorMarkers():
    return {
        "floor0marker": pygame.transform.scale(pygame.image.load(resource_path("data/floor0marker.png")).convert_alpha(), (150, 150)),
        "floor1marker": pygame.transform.scale(pygame.image.load(resource_path("data/floor1marker.png")).convert_alpha(), (150, 150)),
        "floor2marker": pygame.transform.scale(pygame.image.load(resource_path("data/floor2marker.png")).convert_alpha(), (150, 150)),
        "floor3marker": pygame.transform.scale(pygame.image.load(resource_path("data/floor3marker.png")).convert_alpha(), (150, 150))
    }

def SourceBoard():
    return {
        "source_board": pygame.image.load(resource_path("data/source_board.png")).convert_alpha()
    }

# Electricity Meter
def ElectricityMeter():
    return {
        "elec0": pygame.image.load(resource_path("data/noelec.png")).convert_alpha(),
        "elec1": pygame.image.load(resource_path("data/elec1.png")).convert_alpha(),
        "elec2": pygame.image.load(resource_path("data/elec2.png")).convert_alpha(),
        "elec3": pygame.image.load(resource_path("data/elec3.png")).convert_alpha(),
        "elec4": pygame.image.load(resource_path("data/elec4.png")).convert_alpha(),
        "elec5": pygame.image.load(resource_path("data/elec5.png")).convert_alpha()
    }