import pygame
import sys
import os

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

dt = 0
clock = pygame.time.Clock()
pos = None

def LoadWorkerBlue():
    return {
        "blue_right": pygame.transform.scale(pygame.image.load(resource_path("data/worker.png")).convert_alpha(), (63, 64)),
        "blue_left": pygame.transform.scale(pygame.image.load(resource_path("data/worker_left.png")).convert_alpha(), (63, 64)) 
    }

def LoadWorkerBrown():
    return {
        "brown_right": pygame.transform.scale(pygame.image.load(resource_path("data/worker1.png")).convert_alpha(), (63, 64)),
        "brown_left": pygame.transform.scale(pygame.image.load(resource_path("data/worker1_left.png")).convert_alpha(), (63, 64)) 
    }

def LoadWorkerGrey():
    return {
        "grey_right": pygame.transform.scale(pygame.image.load(resource_path("data/worker2.png")).convert_alpha(), (63, 64)),
        "grey_left": pygame.transform.scale(pygame.image.load(resource_path("data/worker2_left.png")).convert_alpha(), (63, 64)) 
    }

art = {}
art.update(LoadWorkerBlue())
art.update(LoadWorkerBrown())
art.update(LoadWorkerGrey())

animation_angles = [0, 15, 30, 15, 0, -15, -30, -15]

worker_frames = []
for angle in animation_angles:
    rotated_image = pygame.transform.rotate(art["blue_right"], angle)
    worker_frames.append(rotated_image)

brown_worker_frames = []
for angle in animation_angles:
    rotated_image = pygame.transform.rotate(art["brown_right"], angle)
    brown_worker_frames.append(rotated_image)

grey_worker_frames = []
for angle in animation_angles:
    rotated_image = pygame.transform.rotate(art["grey_right"], angle)
    grey_worker_frames.append(rotated_image)

current_frame = 0
anim_timer = 0
frame_duration = 100