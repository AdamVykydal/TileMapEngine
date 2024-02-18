import pygame 
from Renderer import Renderer
from TileMap import TileMap
from Coords import Coords
from HandleEvents import HandleEvents
from loadTextures import LoadTextures
from MapUpdate import MapUpdate
import copy



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.renderer = Renderer()
        self.mapWidt = 100
        self.mapHeight = 100
        self.textures = LoadTextures.run()
        self.tileMapTerrein = TileMap(self.textures, self.mapWidt, self.mapHeight)
        self.tileMapObjects = TileMap(self.textures, self.mapWidt, self.mapHeight)
        self.clock = pygame.time.Clock()
        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.handleEvents = HandleEvents(self.screenWidth, self.screenHeight, self.mapWidt, self.mapHeight)
        self.mapUpdate = MapUpdate(self.textures)
        
        print(self.textures)
        
   
    def run(self):
        while True:
            self.clock.tick()
            mousePosX, mousePosY = pygame.mouse.get_pos()
            self.startPoint = self.handleEvents.cameraMouseMove(mousePosX, mousePosY)
            self.scale, self.startPoint, mousePressed = self.handleEvents.check()
            self.screen.fill((0, 0, 0))
            self.mapUpdate.manageChuncks(self.screen, self.tileMapTerrein.chunks, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #print(sys.getsizeof(self.tileMapTerrein.chunks))
            #self.screen.blit(self.tileMapTerrein.chunks[0][0].surface, (50,50)) 
            #print(self.startPoint.x, self.startPoint.y)
            #self.renderer.renderChunks(self. screen, self.tileMapTerrein.chunks, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #self.renderer.renderTerrein(self. screen, self.tileMapTerrein.tiles, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #self.renderer.renderObjects(self. screen, self.tileMapObjects.tiles, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            
            pygame.display.update()
            #print(self.clock.get_fps())