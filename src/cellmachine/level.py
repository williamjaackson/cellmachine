from PIL import Image
from pathlib import Path

texturepack = {}
filenames = [
    "0",
    "BGDefault",
    "ccw",
    "cw",
    "enemy",
    "generator",
    "immobile",
    "mover",
    "push",
    "slide",
    "trash"
]

# get the current files path
path = Path(__file__).parent
# have /textures/ be the current path
path = Path(path, "textures")

# load all the textures
for filename in filenames:
    image = Image.open(Path(path, filename + ".png"))
    image = image.convert("RGBA")
    texturepack[filename] = [image]

# create rotations
for filename in filenames:
    image = texturepack[filename][0]
    for i in range(1, 4):
        texturepack[filename].append(image.rotate(-90 * i))

class Level:
    def __init__(self, size, cells = None, placeables = None, tutorial_text: str = "", name: str = ""):
        self.size       = size
        self.cells      = {}
        self.placeables = [] if placeables is None else placeables

        for cell in cells or []:
            cell.level = self
            self.cells[cell.position] = cell
        
        self.tick_count = 0

        self.tutorial_text = tutorial_text
        self.name = name
    
    def outside_bounds(self, position):
        if position[0] < 0 or position[0] >= self.size[0]:
            return True
        if position[1] < 0 or position[1] >= self.size[1]:
            return True
        return False

    def subtick(self, celltype, rotation=-1):
        update_queue = []

        for cell in self.cells.values():
            if cell.celltype == celltype and (rotation == -1 or cell.rotation == rotation):
                update_queue.append(cell)

        for cell in update_queue:
            print(cell.celltype, cell.position, cell.rotation)

        if rotation != -1:
            update_queue.sort(key=lambda cell: cell.position[rotation % 2], reverse=rotation <= 2)
        
        for cell in update_queue:
            print(cell.celltype, cell.position, cell.rotation)
            cell.step()
    
    def tick(self, count=1):
        subticks = [
            ('generator', 0), 
            ('generator', 2),
            ('generator', 3),
            ('generator', 1),

            ('cw', -1),
            ('ccw', -1),

            ('mover', 0),
            ('mover', 2),
            ('mover', 3),
            ('mover', 1),
        ]

        for _ in range(count):
            for subtick in subticks:
                self.subtick(*subtick)
            
            self.tick_count += 1
    
    def preview(self, image_size=None):
        texture_size = 16

        image_width, image_height = self.size[0] * texture_size, self.size[1] * texture_size

        image = Image.new("RGBA", (image_width, image_height), (41, 41, 41, 255))

        # background
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                image.paste(texturepack["BGDefault"][0], (x * texture_size, y * texture_size))

        # placeables
        for x, y in self.placeables:
            image.paste(texturepack["0"][0], (x * texture_size, y * texture_size))
        
        # cells
        for cell in self.cells.values():
            image.paste(texturepack[cell.celltype][cell.rotation], (cell.position[0] * texture_size, cell.position[1] * texture_size))
        
        if image_size is not None:
            if image_width > image_height:
                image = image.resize((image_size, int(image_size * image_height / image_width)), resample=Image.NEAREST)
            else:
                image = image.resize((int(image_size * image_width / image_height), image_size), resample=Image.NEAREST)
        
        return image