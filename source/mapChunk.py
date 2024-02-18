import pygame 
class mapChunk:
    def __init__(self, textures, w, h) -> None:
        self.tiles = [[0 for x in range(w)] for y in range(h)]
        self.tiles[0][0] = 1
        self.tiles[4][4] = 1
        self.tiles[0][4] = 1
        self.tiles[4][0] = 1
       
        self.surface = pygame.Surface((w*32, h*32))
        self.update(textures)
    
    def update(self, textures):
        for y, row in enumerate(self.tiles):
           for x ,tile in enumerate(row):
                if tile == 0:   
                    self.surface.blit(textures["grass"], (x * 32,y * 32))
                if tile == 1:   
                    self.surface.blit(textures["sand"], (x * 32,y * 32))


#mapChunk(10,10)