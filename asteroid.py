import pygame 
from constants import *
from circleshape import *
from logger import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
    def draw(self, thing):
        pygame.draw.circle(thing,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_num = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_num)
        vector2 = self.velocity.rotate(random_num * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_one.velocity = vector1 * 1.2
        asteroid_two.velocity = vector2 * 1.2
