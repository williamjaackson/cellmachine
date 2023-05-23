from .cell import Cell

class Slide(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'slide', position, rotation)
    
    def push(self, direction, bias):
        if direction == self.rotation or direction == (self.rotation + 2) % 4:
            return super().push(direction, bias)
        return False, False