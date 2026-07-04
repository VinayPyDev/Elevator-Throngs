import pygame
import moderngl

ctx = moderngl.create_context()

with open("shaders/vertex.glsl") as f:
    vertex = f.read()
with open("shaders/fragment.glsl") as f:
    fragment = f.read()

program = ctx.program(
    vertex_shader=vertex,
    fragment_shader=fragment
)