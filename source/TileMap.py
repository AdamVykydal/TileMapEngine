from mapChunk import mapChunk
class TileMap:
    def __init__(self, textures, w, h):
        chunkW = 5
        chunkH = 5
        chunksX = w // chunkW
        chunksY = h // chunkH
        self.tiles = [[0 for x in range(w)] for y in range(h)]  
        self.chunks = [[mapChunk(textures ,chunkW,chunkH) for x in range(chunksX)] for y in range(chunksY)]
        """
        for chunkRow in self.chunks:
            for chunk in chunkRow:
                for tiles in chunk.tiles:
                    #print(tiles)
                    pass
        """
       
        #a= [sublist[2:9] for sublist in self.tiles]
       

#TileMap(20,20)
    