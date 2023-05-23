from .cell import Cell

class CW(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'cw', position, rotation)
    
    def step(self):
        rotation_offsets = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]

        for offset in rotation_offsets:
            target = (self.position[0] + offset[0], self.position[1] + offset[1])
            cell = self.level.cells.get(target)
            if cell is not None:
                cell.rotation += 1
