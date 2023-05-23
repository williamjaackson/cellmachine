from .cell import Cell

class Mover(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'mover', position, rotation)
    
    def step(self):
        self.push(self.rotation, 0)
    
    def push(self, direction, bias):
        if direction == self.rotation:
            bias += 1
        
        if direction == (self.rotation + 2) % 4:
            bias -= 1
        
        return super().push(direction, bias)

