class TileMap:
    def __init__(self, w, h):
        self.tiles = [[0 for x in range(w)] for y in range(h)]  
        
    