from ..level import Level
from ..cells import *

def format_cells(cells, placeables, width, height):
    _placeables = set()
    _cells = []

    celltype = {
        0: Generator,
        1: CW,
        2: CCW,
        3: Mover,
        4: Slide,
        5: Push,
        6: Immobile,
        7: Enemy,
        8: Trash,
        9: "BGDefault",
        10: "0",
    }

    if placeables  != "":
        for placeable in placeables.split(","):
            x, y = placeable.split(".")
            y = height - int(y) - 1
            _placeables.add((int(x), int(y)))

    if cells != "":
        for cell in cells.split(","):
            _type, _rotation, x, y = cell.split(".")
            y = height - int(y) - 1
            _cell = celltype[int(_type)](
                level=None,
                position=(int(x), int(y)),
                rotation=int(_rotation),
            )
            _cells.append(_cell)
    
    return _placeables, _cells

def import_level(level_string):
    string_components = level_string.split(";")

    components = {
        'version': string_components[0],
        'width': int(string_components[1]),
        'height': int(string_components[2]),
        'placeables': string_components[3],
        'cells': string_components[4],
        'tutorial_text': string_components[5],
        'name': string_components[6],
    }

    placeables, cells = format_cells(components['cells'], components['placeables'], components['width'], components['height'])

    level_data = {
        'size': (components['width'], components['height']),
        'placeables': placeables,
        'cells': cells,
        'tutorial_text': components['tutorial_text'],
        'name': components['name'],
    }

    lvl = Level(
        size=level_data['size'],
        cells=cells,
        placeables=level_data['placeables'],
        name=level_data['name'],
        tutorial_text=level_data['tutorial_text'],
    )
    return lvl

def export_level(level):
    celltype = {
        "generator": 0,
        "cw": 1,
        "ccw": 2,
        "mover": 3,
        "slide": 4,
        "push": 5,
        "immobile": 6,
        "enemy": 7,
        "trash": 8,
        "BGDefault": 9,
        "0": 10,
    }

    placeables = ""
    cells = ""

    for placeable in level.placeables:
        placeables += f'{placeable[0]}.{level.size[1] - placeable[1] - 1},'
    placeables = placeables[:-1]

    for cell in level.cells.values():
        cells += f'{celltype[cell.celltype]}.{cell.rotation}.{cell.position[0]}.{level.size[1] - cell.position[1] - 1},'
    cells = cells[:-1]

    level_string = f'V1;{level.size[0]};{level.size[1]};{placeables};{cells};{level.tutorial_text};{level.name};'

    return level_string