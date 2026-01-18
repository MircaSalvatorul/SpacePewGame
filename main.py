import pygame
from os.path import join

from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (Window_Width/2,Window_Height/2))
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        # input
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('Fire Laser')

class Star(pygame.sprite.Sprite):
    def __init__(self,groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, Window_Width),randint(0, Window_Height)))


#setup
pygame.init()
Window_Width,Window_Height = 1280,720
display_surface = pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption('Space Pew')
running = True
clock = pygame.time.Clock()



#plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100


all_sprites = pygame.sprite.Group()
star_surf =  pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
    Star(all_sprites,star_surf)
player = Player(all_sprites)


meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (Window_Width/2, Window_Height/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, Window_Height-20))




while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    #draw game
    display_surface.fill('darkgray')

    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()