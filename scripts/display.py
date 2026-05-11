import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

class ElevatorUp():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image
    
def RenderElevatorUp():
    img = pygame.image.load(resource_path("data/Sprite-0001-sheet.png")).convert()  
    SpriteSheet = ElevatorUp(img)
    frames = 14
    width, height = 64, 104
    x_offset = 29
    scale = 2.0
    colorkey = (0, 0, 0) 

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

class ElevatorDown():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color, x_offset=0):
        image = pygame.Surface((width, height))  
        image.fill(color)
        image.blit(self.sheet, (0, 0), (x_offset + frame * width, 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image
    
def RenderElevatorDown():
    img = pygame.image.load(resource_path("data/Sprite-0001-2-sheet.png")).convert()  
    SpriteSheet = ElevatorDown(img)
    frames = 14
    width, height = 64, 104
    x_offset = 29
    scale = 2.0
    colorkey = (0, 0, 0)  

    animation_list = []
    for i in range(frames):
        animation_list.append(SpriteSheet.get_image(i, width, height, scale, colorkey, x_offset))

    return animation_list

# Render funcs for elevator buttons
def RenderButtonFloor0(screen, art):
    screen.blit(art["button1"], (560 - 20, 642 - 8))
def RenderButtonFloor1(screen, art):
    screen.blit(art["button1"], (560 - 20, 532))
def RenderButtonFloor2(screen, art):
    screen.blit(art["button1"], (560 - 20, 426))
def RenderButtonFloor3(screen, art):
    screen.blit(art["button1"], (560 - 20, 326))

def RenderButtonMovingUp(screen, art):
    screen.blit(art["button2"], (560 - 20, 642 - 8))
def RenderButtonMovingUp1(screen, art):
    screen.blit(art["button2"], (560 - 20, 532))
def RenderButtonMovingUp2(screen, art):
    screen.blit(art["button2"], (560 - 20, 426))
def RenderButtonMovingUp3(screen, art):
    screen.blit(art["button2"], (560 - 20, 326))

def RenderButtonMovingDown(screen, art):
    screen.blit(art["button3"], (560 - 20, 642 - 8))
def RenderButtonMovingDown1(screen, art):
    screen.blit(art["button3"], (560 - 20, 532))
def RenderButtonMovingDown2(screen, art):
    screen.blit(art["button3"], (560 - 20, 426))
def RenderButtonMovingDown3(screen, art):
    screen.blit(art["button3"], (560 - 20, 326))

# Floor Markers
def RenderFloor0Marker(screen, art):
    screen.blit(art["floor0marker"], (1130, 0))
def RenderFloor1Marker(screen, art):
    screen.blit(art["floor1marker"], (1130, 0))
def RenderFloor2Marker(screen, art):
    screen.blit(art["floor2marker"], (1130, 0))
def RenderFloor3Marker(screen, art):
    screen.blit(art["floor3marker"], (1130, 0))