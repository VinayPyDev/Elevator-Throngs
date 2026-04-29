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