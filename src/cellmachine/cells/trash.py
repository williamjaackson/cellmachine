from .cell import Cell

class Trash(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'trash', position, rotation)
    
    def push(self, direction, bias):
        if bias > 0:
            return True, True
        return False, False