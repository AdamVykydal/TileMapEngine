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
        self.oldObjectScale = 32
        self.oldTerreinScale = 32
        self.texture1 = pygame.transform.scale(self.originalTextureHouse1, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture2 = pygame.transform.scale(self.originalTextureHouse2, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture3 = pygame.transform.scale(self.originalTextureHouse3, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture4 = pygame.transform.scale(self.originalTextureHouse4, (self.oldTerreinScale, self.oldTerreinScale))
        self.grass = pygame.transform.scale(self.originalTextureGrass, (self.oldTerreinScale, self.oldTerreinScale))
        self.sand = pygame.transform.scale(self.originalTextureSand, (self.oldTerreinScale, self.oldTerreinScale))
        self.screenEndY = 1080 + self.oldTerreinScale
        self.screenEndX = 1920 + self.oldTerreinScale
        
    def renderTerrein(self, screen, tiles, scale, startPointCoords, mousePressed, mousePos):
        self.startPointCoords = copy.copy(startPointCoords)
        if not self.oldTerreinScale == scale:
            self.grass = pygame.transform.scale(self.originalTextureGrass, (scale, scale))
            self.sand = pygame.transform.scale(self.originalTextureSand, (scale, scale))
            #self.screenEndY = 1080 + scale
            #self.screenEndX = 1920 + scale
            self.oldTerreinScale = scale
            
        rowIndex = 0
        
        #startTileY = startPointCoords.y // scale
        #startTileY = abs(startTileY)
        #startTileX = startPointCoords.x // scale
        #startTileX = abs(startTileX)
       
        #print(startTileY)
        #print(startTileX)
        
        for row in tiles:
            self.startPointCoords.x = copy.deepcopy(startPointCoords.x)
            tileIndex = 0
            
            for tile in row:
                if self.startPointCoords.y >= -scale and self.startPointCoords.y <= 1080 and self.startPointCoords.x >= -scale and self.startPointCoords.x <= 1920:
                    
                    if tile == 0:
                        #rectangle = self.grass.get_rect(topleft= (self.coords.x, self.coords.y))
                    
                        #if rectangle.collidepoint(mousePos) and mousePressed:
                            #tiles[rowIndex][tileIndex] = 2.1
                            #tiles[rowIndex][tileIndex + 1] = 2.2
                            #tiles[rowIndex - 1][tileIndex ] = 2.3
                            #tiles[rowIndex - 1][tileIndex + 1] = 2.4

                        
                        screen.blit(self.grass, (self.startPointCoords.x, self.startPointCoords.y))
                        
                    
                    elif tile == 1:
                        rectangle = self.sand.get_rect(topleft= (self.startPointCoords.x, self.startPointCoords.y))
                        
                        if rectangle.collidepoint(mousePos) and mousePressed:
                            tiles[rowIndex][tileIndex] = 0
                        
                        screen.blit(self.sand, rectangle)
                
                tileIndex += 1
                self.startPointCoords.x += scale
            
            self.startPointCoords.y += scale
            rowIndex += 1
        
    def renderObjects(self, screen, tiles, scale, coords, mousePressed, mousePos):
        self.startPointCoords = copy.deepcopy(coords)
        if not self.oldObjectScale == scale:
            self.texture1 = pygame.transform.scale(self.originalTextureHouse1, (scale, scale))
            self.texture2 = pygame.transform.scale(self.originalTextureHouse2, (scale, scale))
            self.texture3 = pygame.transform.scale(self.originalTextureHouse3, (scale, scale))
            self.texture4 = pygame.transform.scale(self.originalTextureHouse4, (scale, scale))
            #self.screenEndY = 1080 + scale
            #self.screenEndX = 1920 + scale
            self.oldObjectScale = scale
        
        rowIndex = 0
        
        for row in tiles:
            self.startPointCoords.x = copy.copy(coords.x)
            tileIndex = 0
            

            for tile in row:
                    
                if self.startPointCoords.x >= -scale and self.startPointCoords.y >= -scale and self.startPointCoords.x <= 1920 and self.startPointCoords.y <= 1080:
                    
                    if mousePressed:
                            
                            rectangle = pygame.Rect(self.startPointCoords.x, self.startPointCoords.y, scale,scale)
                            
                            if rectangle.collidepoint(mousePos):
                                tiles[rowIndex][tileIndex] = 1.1
                                tiles[rowIndex][tileIndex + 1] = 1.2
                                tiles[rowIndex - 1][tileIndex ] = 1.3
                                tiles[rowIndex - 1][tileIndex + 1] = 1.4
                    
                    if tile == 1.1:
                        
                        screen.blit(self.texture1, (self.startPointCoords.x, self.startPointCoords.y))
                    elif tile == 1.2:
                                                
                        screen.blit(self.texture2, (self.startPointCoords.x, self.startPointCoords.y))
                    elif tile == 1.3:
                        
                        screen.blit(self.texture3, (self.startPointCoords.x, self.startPointCoords.y))
                    elif tile == 1.4:
                        
                        screen.blit(self.texture4, (self.startPointCoords.x, self.startPointCoords.y))
                
                tileIndex += 1
                self.startPointCoords.x += scale
        
            self.startPointCoords.y += scale
            rowIndex += 1    