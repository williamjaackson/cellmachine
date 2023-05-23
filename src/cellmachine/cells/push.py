from .cell import Cell

class Push(Cell): 
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'push', position, rotation)