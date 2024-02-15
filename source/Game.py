import pygame 
from Renderer import Renderer
from TileMap import TileMap
from Coords import Coords
from HandleEvents import HandleEvents
import threading
import copy

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.renderer = Renderer()
        self.mapWidt = 200
        self.mapHeight = 200
        self.tileMapTerrein = TileMap(self.mapWidt, self.mapHeight)
        self.tileMapObjects = TileMap(self.mapWidt, self.mapHeight)
        self.clock = pygame.time.Clock()
        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.handleEvents = HandleEvents(self.screenWidth, self.screenHeight, self.mapWidt, self.mapHeight)
   
    def run(self):
        while True:
            self.clock.tick(60)
            mousePosX, mousePosY = pygame.mouse.get_pos()
            self.startPoint = self.handleEvents.cameraMouseMove(mousePosX, mousePosY)
            self.scale, self.startPoint, mousePressed = self.handleEvents.check()
            self.screen.fill((0, 0, 0))
            self.renderer.renderTerrein(self. screen, self.tileMapTerrein.tiles, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            self.renderer.renderObjects(self. screen, self.tileMapObjects.tiles, self.scale, copy.copy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            pygame.display.update()
            print(self.clock.get_fps())