class TileMap:
    def __init__(self, w, h):
        self.tiles = [[0 for x in range(w)] for y in range(h)]  
        self.tiles[9][1] = 1
        self.tiles[2][2] = 1
        self.tiles[200][5] = 1
        self.tiles[200][250] = 1
        
    