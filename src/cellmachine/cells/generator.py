from .cell import Cell

class Generator(Cell):
    def __init__(self, level, position, rotation=0):
        super().__init__(level, 'generator', position, rotation)
    
    def step(self):
        offset = [0, 0]

        if self.rotation == 0:
            offset[0] += 1
        elif self.rotation == 1:
            offset[1] += 1
        elif self.rotation == 2:
            offset[0] -= 1
        elif self.rotation == 3:
            offset[1] -= 1
        
        newcell_pos   = (self.position[0] + offset[0], self.position[1] + offset[1])
        reference_pos = (self.position[0] - offset[0], self.position[1] - offset[1])

        if self.level.outside_bounds(newcell_pos):
            return
        if self.level.outside_bounds(reference_pos):
            return
    
        reference_cell = self.level.cells.get(reference_pos)

        if self.level.cells.get(reference_pos) is None:
            return
        
        in_the_way = self.level.cells.get(newcell_pos)
        
        if in_the_way is not None:
            push_result = in_the_way.push(self.rotation, 1)
            if push_result[0] == False or push_result[1] == True:
                return
        
        reference_cell.__class__(self.level, newcell_pos, reference_cell.rotation)
