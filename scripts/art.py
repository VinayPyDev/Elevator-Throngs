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
# Elevator Line
def ElevatorLine():
    return {
        "line": pygame.transform.scale(pygame.image.load(resource_path("data/floor line2.png")).convert_alpha(), (155, 720))
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
# Resources
    # Electricity Meter
def ElectricityMeter():
    return {
        "elec0": pygame.transform.scale(pygame.image.load(resource_path("data/noelec.png")).convert_alpha(), (100, 100)),
        "elec1": pygame.transform.scale(pygame.image.load(resource_path("data/elec1.png")).convert_alpha(), (100, 100)),
        "elec2": pygame.transform.scale(pygame.image.load(resource_path("data/elec2.png")).convert_alpha(), (100, 100)),
        "elec3": pygame.transform.scale(pygame.image.load(resource_path("data/elec3.png")).convert_alpha(), (100, 100)),
        "elec4": pygame.transform.scale(pygame.image.load(resource_path("data/elec4.png")).convert_alpha(), (100, 100)),
        "elec5": pygame.transform.scale(pygame.image.load(resource_path("data/elec5.png")).convert_alpha(), (100, 100))
    }

    # Weight Meter
def WeightMeter():
    return {
        "wt150": pygame.transform.scale(pygame.image.load(resource_path("data/wt150.png")).convert_alpha(), (100, 100)),
        "wt250": pygame.transform.scale(pygame.image.load(resource_path("data/wt250.png")).convert_alpha(), (100, 100)),
        "wt300": pygame.transform.scale(pygame.image.load(resource_path("data/wt300.png")).convert_alpha(), (100, 100)),
        "wt350": pygame.transform.scale(pygame.image.load(resource_path("data/wt350.png")).convert_alpha(), (100, 100)),
        "wt400": pygame.transform.scale(pygame.image.load(resource_path("data/wt400.png")).convert_alpha(), (100, 100))
    }

    # Repair Meter
def RepairMeter():
    return {
        "repair0": pygame.transform.scale(pygame.image.load(resource_path("data/repair0.png")).convert_alpha(), (100, 100)),
        "repair1": pygame.transform.scale(pygame.image.load(resource_path("data/repair1.png")).convert_alpha(), (100, 100)),
        "repair2": pygame.transform.scale(pygame.image.load(resource_path("data/repair2.png")).convert_alpha(), (100, 100)),
        "repair3": pygame.transform.scale(pygame.image.load(resource_path("data/repair3.png")).convert_alpha(), (100, 100)),
        "repair4": pygame.transform.scale(pygame.image.load(resource_path("data/repair4.png")).convert_alpha(), (100, 100)),
        "repair5": pygame.transform.scale(pygame.image.load(resource_path("data/repair5.png")).convert_alpha(), (100, 100))
    }

# workers 