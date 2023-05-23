from .cell import Cell

class Enemy(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'enemy', position, rotation)
    
    def push(self, direction, bias):
        if bias < 1:
            return False, False
        
        del self.level.cells[self.position]

        return True, True
    
    