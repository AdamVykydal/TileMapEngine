import pygame
from Coords import Coords
import copy

class Renderer:
    def __init__(self):
        self.originaTexture0 = pygame.image.load("recources\img\\0.png").convert_alpha()
        self.originalTexture1 = pygame.image.load("recources\img\\1.png").convert_alpha()
        
    def render(self, screen, tiles, scale, coords):
        self.coords = copy.copy(coords)
        self.texture0 = pygame.transform.scale(self.originaTexture0, (scale, scale))
        self.texture1 = pygame.transform.scale(self.originalTexture1, (scale, scale))
        
        
        for row in tiles:
            self.coords.x = copy.copy(coords.x)
            
            for tile in row:
                if tile == 0:
                    rectangle = self.texture0.get_rect(topleft= (self.coords.x, self.coords.y))
                    screen.blit(self.texture0, rectangle)
                elif tile == 1:
                    rectangle = self.texture1.get_rect(topleft= (self.coords.x, self.coords.y))
                    screen.blit(self.texture1, rectangle)
                self.coords.x += scale
            
            self.coords.y += scale