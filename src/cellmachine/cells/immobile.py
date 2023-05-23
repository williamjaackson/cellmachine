from .cell import Cell

class Immobile(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'immobile', position, rotation)
    
    def push(self, direction, bias):
        return False, False

    @Cell.rotation.setter
    def rotation(self, value): ...