class Cell:
    def __init__(self, level, celltype, position, rotation=0):
        self.level    = level
        self.celltype = celltype
        self._rotation = rotation

        self._position = position
        if level is not None:
            self.position = position
    
    @property
    def rotation(self):
        return self._rotation
    
    @rotation.setter
    def rotation(self, value: int):
        self._rotation = value % 4
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value: tuple):
        del self.level.cells[self._position]
        self._position = value
        self.level.cells[self._position] = self

    def push(self, direction, bias):
        """
        Returns
        -------
            - (bool) Can the cell move?
            - (bool) Does the previous cell, the one pushing this one, get deleted?
        """
        target = [*self.position]

        if direction == 0: # Right
            target[0] += 1
        elif direction == 1: # Down
            target[1] += 1
        elif direction == 2: # Left
            target[0] -= 1
        elif direction == 3: # Up
            target[1] -= 1
        
        target = tuple(target)

        if self.level.outside_bounds(target):
            return False, False
        
        if bias < 1:
            return False, False
        
        future_cell = self.level.cells.get(target)
    
        if future_cell is None:
            self.position = target
            return True, False

        push_result = future_cell.push(direction, bias)

        if push_result[1]: # the cell we pushed deletes us
            del self.level.cells[self.position]
            return True, False
        
        if push_result[0]: # the cell we pushed moved
            self.position = target
            return True, False
    
        return False, False
    
    def step(self):
        ...
    
    def __repr__(self):
        return f'{self.celltype}[{self.rotation}]'