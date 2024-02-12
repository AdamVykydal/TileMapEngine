class TileMap:
    def __init__(self):
        w, h = 100, 100
        self.Matrix = [[0 for x in range(w)] for y in range(h)]  
        self.Matrix[0][1] = 1
        for w in self.Matrix:
            print(w)
   
TileMap()