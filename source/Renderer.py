import pygame

import copy

class Renderer:
    def __init__(self, startPoint):
        self.originalTextureGrass = pygame.image.load("recources\img\grass.png").convert()
        self.originalTextureSand = pygame.image.load("recources\img\sand.png").convert()
        self.originalTextureHouse1 = pygame.image.load("recources\img\House1.png").convert_alpha()
        self.originalTextureHouse2 = pygame.image.load("recources\img\House2.png").convert_alpha()
        self.originalTextureHouse3 = pygame.image.load("recources\img\House3.png").convert_alpha()
        self.originalTextureHouse4 = pygame.image.load("recources\img\House4.png").convert_alpha()
        self.oldObjectScale = 0
        self.oldTerreinScale = 4800
        self.oldStartPointCoords = startPoint
        self.oldStartPointCoords.x = 10
        self.texture1 = pygame.transform.scale(self.originalTextureHouse1, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture2 = pygame.transform.scale(self.originalTextureHouse2, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture3 = pygame.transform.scale(self.originalTextureHouse3, (self.oldTerreinScale, self.oldTerreinScale))
        self.texture4 = pygame.transform.scale(self.originalTextureHouse4, (self.oldTerreinScale, self.oldTerreinScale))
        self.grass = pygame.transform.scale(self.originalTextureGrass, (self.oldTerreinScale, self.oldTerreinScale))
        self.sand = pygame.transform.scale(self.originalTextureSand, (self.oldTerreinScale, self.oldTerreinScale))
        self.mapOnScreen = None
        #self.surface = pygame.Surface(self.oldTerreinScale,self.oldTerreinScale)
        
        self.screenEndY = 1080 + self.oldTerreinScale
        self.screenEndX = 1920 + self.oldTerreinScale
        
    def renderScaleMap(self, screen, mapSurface, scale, startPointCoords):
        
 
        #if startPointCoords.x != self.oldStartPointCoords.x or startPointCoords.y != self.oldStartPointCoords.y:
            #self.mapOnScreen = mapSurface.subsurface(abs(startPointCoords.x),abs(startPointCoords.y), scale, scale)
            #self.oldStartPointCoords = startPointCoords
            
        #if scale != self.oldTerreinScale:
            #self.mapOnScreen = pygame.transform.scale(self.mapOnScreen, (scale,scale))
            #self.oldTerreinScale = scale
            
        screen.blit(mapSurface,(startPointCoords.x, startPointCoords.y))
            

   
    def renderChunks(self, screen, scale, chunkSurface, startPointCoords):
        return screen.blit(pygame.transform.scale(chunkSurface, (scale,scale)),(startPointCoords.x, startPointCoords.y))
        
        
    
    def renderTerrein(self, screen, tiles, scale, startPointCoords, mousePressed, mousePos):
        #print(startPointCoords.x, startPointCoords.y)
        self.startPointCoords = copy.deepcopy(startPointCoords)
        if not self.oldTerreinScale == scale:
            self.grass = pygame.transform.scale(self.originalTextureGrass, (scale, scale))
            self.sand = pygame.transform.scale(self.originalTextureSand, (scale, scale))
            #self.screenEndY = 1080 + scale
            #self.screenEndX = 1920 + scale
            self.oldTerreinScale = scale
            
        #print("start:",startPointCoords.x, startPointCoords.y)
        
        #startTileY = startPointCoords.y // scale
        #startTileY = abs(startTileY)
        #startTileX = startPointCoords.x // scale
        #startTileX = abs(startTileX)
        #endTileY = startTileY + (1080 // scale)
        #endTileX = startTileX + (1920 // scale)
       
        #print(startTileY)
        #print(startTileX)
        
        #print("starTile:", startTileX, startTileY)
        #print("endTile:", endTileX, endTileY)
        
        
        #print(startTileX, "/", endTileX, startTileY,"/", endTileY)
        #screenTiles = [sublist[startTileX:endTileX] for sublist in tiles[startTileY:endTileY]]
        
        #print("before:",startPointCoords.x, startPointCoords.y)
        #print(screenTiles)
        rowIndex = 0
        
        for row in tiles:
            self.startPointCoords.x = copy.deepcopy(startPointCoords.x)
            #print(self.startPointCoords.x, self.startPointCoords.y)
            tileIndex = 0
            
            
            #print(screenTiles)
            for tile in row:
                
                #print("In:",startPointCoords.x, startPointCoords.y)
                if self.startPointCoords.y >= -scale and self.startPointCoords.y <= 1080 and self.startPointCoords.x >= -scale and self.startPointCoords.x <= 1920:
                    
                    if tile == 0:
                    
                        #if rectangle.collidepoint(mousePos) and mousePressed:
                            #tiles[rowIndex][tileIndex] = 2.1
                            #tiles[rowIndex][tileIndex + 1] = 2.2
                            #tiles[rowIndex - 1][tileIndex ] = 2.3
                            #tiles[rowIndex - 1][tileIndex + 1] = 2.4

                        #print(self.startPointCoords.x, self.startPointCoords.y)
                        screen.blit(self.grass, (self.startPointCoords.x, self.startPointCoords.y))
                        #print(a.x, a.y)
                        
                    
                    elif tile == 1:
                        rectangle = self.sand.get_rect(topleft= (self.startPointCoords.x, self.startPointCoords.y))
                        
                        if rectangle.collidepoint(mousePos) and mousePressed:
                            tiles[rowIndex][tileIndex] = 1
                        
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