import pygame

import copy

class Renderer:
    def __init__(self):
        self.originalTextureGrass = pygame.image.load("recources\img\grass.png").convert_alpha()
        self.originalTextureSand = pygame.image.load("recources\img\sand.png").convert_alpha()
        self.originalTextureHouse1 = pygame.image.load("recources\img\House1.png").convert_alpha()
        self.originalTextureHouse2 = pygame.image.load("recources\img\House2.png").convert_alpha()
        self.originalTextureHouse3 = pygame.image.load("recources\img\House3.png").convert_alpha()
        self.originalTextureHouse4 = pygame.image.load("recources\img\House4.png").convert_alpha()
        self.scale = 32
        self.texture1 = pygame.transform.scale(self.originalTextureHouse1, (self.scale, self.scale))
        self.texture2 = pygame.transform.scale(self.originalTextureHouse2, (self.scale, self.scale))
        self.texture3 = pygame.transform.scale(self.originalTextureHouse3, (self.scale, self.scale))
        self.texture4 = pygame.transform.scale(self.originalTextureHouse4, (self.scale, self.scale))
        self.grass = pygame.transform.scale(self.originalTextureGrass, (self.scale, self.scale))
        self.sand = pygame.transform.scale(self.originalTextureSand, (self.scale, self.scale))
        self.screenEndY = 1080 + self.scale
        self.screenEndX = 1920 + self.scale
        
    def renderTerrein(self, screen, tiles, scale, coords, mousePressed, mousePos):
        self.coords = copy.copy(coords)
        if not self.scale == scale:
            self.grass = pygame.transform.scale(self.originalTextureGrass, (scale, scale))
            self.sand = pygame.transform.scale(self.originalTextureSand, (scale, scale))
            #self.screenEndY = 1080 + scale
            #self.screenEndX = 1920 + scale
            self.scale = scale
            
        rowIndex = 0
        
        for row in tiles:
            self.coords.x = copy.deepcopy(coords.x)
            tileIndex = 0
            
            for tile in row:
                if self.coords.y >= -scale and self.coords.y <= 1080 and self.coords.x >= -scale and self.coords.x <= 1920:
                    
                    if tile == 0:
                        #rectangle = self.grass.get_rect(topleft= (self.coords.x, self.coords.y))
                    
                        #if rectangle.collidepoint(mousePos) and mousePressed:
                            #tiles[rowIndex][tileIndex] = 2.1
                            #tiles[rowIndex][tileIndex + 1] = 2.2
                            #tiles[rowIndex - 1][tileIndex ] = 2.3
                            #tiles[rowIndex - 1][tileIndex + 1] = 2.4

                        
                        screen.blit(self.grass, (self.coords.x, self.coords.y))
                        
                    
                    elif tile == 1:
                        rectangle = self.sand.get_rect(topleft= (self.coords.x, self.coords.y))
                        
                        if rectangle.collidepoint(mousePos) and mousePressed:
                            tiles[rowIndex][tileIndex] = 0
                        
                        screen.blit(self.sand, rectangle)
                
                tileIndex += 1
                self.coords.x += scale
            
            self.coords.y += scale
            rowIndex += 1
        
    def renderObjects(self, screen, tiles, scale, coords, mousePressed, mousePos):
        self.coords = copy.deepcopy(coords)
        if not self.scale == scale:
            self.texture1 = pygame.transform.scale(self.originalTextureHouse1, (scale, scale))
            self.texture2 = pygame.transform.scale(self.originalTextureHouse2, (scale, scale))
            self.texture3 = pygame.transform.scale(self.originalTextureHouse3, (scale, scale))
            self.texture4 = pygame.transform.scale(self.originalTextureHouse4, (scale, scale))
            #self.screenEndY = 1080 + scale
            #self.screenEndX = 1920 + scale
            self.scale = scale
        
        rowIndex = 0
        
        for row in tiles:
            self.coords.x = copy.copy(coords.x)
            tileIndex = 0
            

            for tile in row:
                    
                if self.coords.x >= -scale and self.coords.y >= -scale and self.coords.x <= 1920 and self.coords.y <= 1080:
                    
                    if mousePressed:
                            
                            rectangle = pygame.Rect(self.coords.x, self.coords.y, scale,scale)
                            
                            if rectangle.collidepoint(mousePos):
                                tiles[rowIndex][tileIndex] = 1.1
                                tiles[rowIndex][tileIndex + 1] = 1.2
                                tiles[rowIndex - 1][tileIndex ] = 1.3
                                tiles[rowIndex - 1][tileIndex + 1] = 1.4
                    
                    if tile == 1.1:
                        
                        screen.blit(self.texture1, (self.coords.x, self.coords.y))
                    elif tile == 1.2:
                                                
                        screen.blit(self.texture2, (self.coords.x, self.coords.y))
                    elif tile == 1.3:
                        
                        screen.blit(self.texture3, (self.coords.x, self.coords.y))
                    elif tile == 1.4:
                        
                        screen.blit(self.texture4, (self.coords.x, self.coords.y))
                
                tileIndex += 1
                self.coords.x += scale
        
            self.coords.y += scale
            rowIndex += 1    