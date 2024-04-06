import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, lane):
        super().__init__()
        self.image = pygame.image.load('./graphics/bullet/SpongeBullet.png')
        self.image = pygame.transform.scale(self.image, (3*2, 1*2))
        self.rect=self.image.get_rect(bottomleft= pos)
        self.lane=lane

    def update(self):
        self.rect.x+=5