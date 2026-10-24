import pygame
import random
from abc import ABC, abstractmethod

class WorkerState(ABC):
    def __init__(self, worker):
        self.worker = worker

    @abstractmethod
    def enter(self): 
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def exit(self):
        pass

class WorkerStateMachine:
    def __init__(self):
        self.current_state = None

    def change_state(self, n_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = n_state
        if self.current_state:
            self.current_state.enter()

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)

class WorkerWalkState(WorkerState):
    def enter(self):
        self.worker.is_moving = True
        self.timer = random.uniform(2.0, 5.0)

    def update(self, dt):
        if self.worker.direction == 1:
            self.worker.pos[0] += self.worker.speed * dt
            if self.worker.rect.right >= 545:
                self.worker.direction = -1
        else:
            self.worker.pos[0] -= self.worker.speed * dt
            if self.worker.rect.left <= 0:
                self.worker.direction = 1

        self.worker.rect.topleft = self.worker.pos

        self.timer -= dt
        if self.timer <= 0:
            if random.choice([True, False]):
                self.worker.state_machine.change_state(WorkerIdleState(self.worker))
            else:
                self.timer = random.uniform(2.0, 5.0)
        if self.worker.elevator_ref and self.worker.elevator_ref.floor == self.worker.floor and self.worker.elevator_ref.is_open:
            self.worker.state_machine.change_state(WorkerElevatorState(self.worker))

    def exit(self):
        pass

class WorkerIdleState(WorkerState):
    def enter(self):
        self.worker.is_moving = False
        self.timer = random.uniform(1.0, 3.0)

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.worker.state_machine.change_state(WorkerWalkState(self.worker))
        if self.worker.elevator_ref and self.worker.elevator_ref.floor == self.worker.floor and self.worker.elevator_ref.is_open:
            self.worker.state_machine.change_state(WorkerElevatorState(self.worker))

    def exit(self):
        pass

class WorkerElevatorState(WorkerState):
    def enter(self):
        self.worker.is_moving = True

    def update(self, dt):
        target_x = 560
        if self.worker.pos[0] < target_x:
            self.worker.pos[0] += self.worker.speed * dt
            self.worker.direction = 1
        elif self.worker.pos[0] > target_x:
            self.worker.pos[0] -= self.worker.speed * dt
            self.worker.direction = -1

        self.worker.rect.topleft = self.worker.pos

        if not self.worker.elevator_ref or self.worker.elevator_ref.floor != self.worker.floor or not self.worker.elevator_ref.is_open:
            self.worker.state_machine.change_state(WorkerWalkState(self.worker))
    
    def exit(self):
        pass