import pygame
from math import cos, sin, radians, atan2, degrees

class Tank(pygame.sprite.Sprite):
    def __init__(self ):
        # init the sprite
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('tank_game/assets/PNG/Retina/tanks_tankNavy3.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.6)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100,500)
        self.shell_group = pygame.sprite.Group()

    def update(self,dt):
        # maybe move the tank
        self.shell_group.update(dt)

    def shoot(self):
        # a new shell is created, and added to shell group
        new_shell = Shell(self.rect.topright)
        self.shell_group.add(new_shell)

    
    def draw(self,screen):
        # blit our tank
        screen.blit(self.image, self.rect)
        # blit ALL of our shells (shell group)
        self.shell_group.draw(screen)
        for s in self.shell_group:
            s.draw(screen)



class Shell(pygame.sprite.Sprite):
    def __init__(self,coords, theta=45):
        # init the sprite
        super().__init__()
        self.x = coords[0]
        self.y = coords[1]
        
        self.theta = theta # in degrees
        self.speed = 20 # meters per second
        self.scale = 1000/50 # pixels per meter

        # make some velocities
        self.dot_x =  self.speed * cos(radians(self.theta))
        self.dot_y = -self.speed * sin(radians(self.theta))

        self.g = 9.81 # gravity in 
        self.m = 1 # 100 kg of mass

        self.og_image = pygame.image.load('tank_game/assets/PNG/Retina/tank_bullet4.png')
        self.og_image = pygame.transform.rotozoom(self.og_image, 0, 0.6)
        self.image = self.og_image # initially shell is not rotated
        self.rect = self.image.get_rect()
        self.rect.center = (coords)
    
    def update(self,dt):
        # calculate our ddot_y
        ddot_y = self.g/self.m # accel in meters/s^2

        # update our dot_y 
        self.dot_y += ddot_y * dt # velocity in m/s

        # put in equations of motion for the shell
        self.x += self.dot_x * self.scale * dt # pos in pixels
        self.y += self.dot_y * self.scale * dt # pos in pixels

        # update our angle, theta
        self.theta = degrees(atan2(-self.dot_y, self.dot_x))

        # check to see if shell is out of bounds
        if self.x > 1000:
            self.kill()
        # update our rect
        self.rect.center = (self.x, self.y)

    def draw(self,screen):
        # rotate the bullet image based on theta
        self.image = pygame.transform.rotate(self.og_image, self.theta)

        # update the rectangle and recenter it
        self.rect = self.image.get_rect(center = self.rect.center)

        screen.blit(self.image, self.rect)

