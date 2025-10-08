import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, angle=0, image=None):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.Vector2(x, y)
        self.angle = angle
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

    def update(self, dt):
        pass

    def update_graphics(self):
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        self.rect = self.image.get_rect(center=(self.pos))

    def draw(self, surface):
        self.update_graphics()
        #surface.blit(self.mask_image, self.rect.topleft)
        surface.blit(self.image, self.rect.topleft)

    def rotate(self, angle):
        self.angle += angle
