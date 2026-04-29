import pygame
pygame.init()
img = pygame.image.load("data/elv_m_2.png")
print(img.get_width(), img.get_height())

img = pygame.image.load("data/elv_m_2.png")
w = img.get_width()
for frames in range(10, 20):
    if w % frames == 0:
        print(f"{frames} frames → {w // frames}px each")

img = pygame.image.load("data/elv_m_2.png")
print(img.get_width(), img.get_height())
# Check frame 0: what's the actual elevator content bounds?
frame0 = pygame.Surface((76, 120))
frame0.blit(img, (0, 0), (0, 0, 76, 120))
pygame.image.save(frame0, "frame0.png")


for i in range(14):
    frame = pygame.Surface((76, 120))
    frame.blit(img, (0, 0), (i * 76, 0, 76, 120))
    pygame.image.save(frame, f"frame_{i}.png")

print("done")