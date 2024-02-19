import pygame
class MapTerrein:
    def __init__(self, textures, w, h):
        self.tiles = [[0 for x in range(w)] for y in range(h)]
        self.surface = pygame.Surface((32*w, 32*h))
        x = 0
        y = 0
        for row in self.tiles:
            x = 0
            
            for tile in row:
                if tile == 0:
                    self.surface.blit(textures["grass"],(x,y))
           
                x += 32
            y += 32
    
    def getSurface(self):
        return self.surface