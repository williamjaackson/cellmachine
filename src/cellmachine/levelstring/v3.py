from ..level import Level
from ..cells import *

base74_key = {char: index for index, char in enumerate("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}")}
def base74_decode(string):
    result = 0
    for char in string:
        result *= 74
        result += base74_key[char]
    return result

def decode_data(encoded_data):
    decoded_data = []

    current_index = 0
    while current_index < len(encoded_data):
        if encoded_data[current_index] in "()":
            if encoded_data[current_index] == ")":
                offset = encoded_data[current_index + 1]
                distance = encoded_data[current_index + 2]
                current_index += 3
            else:
                offset = ""
                current_index += 1
                while encoded_data[current_index] not in "()":
                    offset += encoded_data[current_index]
                    current_index += 1
                if encoded_data[current_index] == ")":
                    distance = encoded_data[current_index + 1]
                    current_index += 1
                else:
                    distance = ""
                    current_index += 1
                    while encoded_data[current_index] != ")":
                        distance += encoded_data[current_index]
                        current_index += 1
                current_index += 1

            offset = -base74_decode(offset)
            distance = base74_decode(distance)

            for d in range(distance):
                decoded_data.append(decoded_data[offset - 1])
        else:
            decoded_data.append(encoded_data[current_index])
            current_index += 1

    return decoded_data

def format_cells(decoded_data, width, height):
    placeables = set()
    cells = []

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

    for index, cell in enumerate(decoded_data):
        cell = base74_decode(cell)

        if cell % 2 == 1:
            x, y = index % width, index // width
            y = height - int(y) - 1
            placeables.add((x, y))
        if cell >= 72:
            continue
        x, y = index % width, index // width
        y = height - int(y) - 1
        _type, _rotation = (cell // 2) % 9, cell // 18

        cells.append(celltype[_type](None, (x, y), _rotation))

    return placeables, cells

def import_level(level_string):
    string_components = level_string.split(";")

    components = {
        'version': string_components[0],
        'width': base74_decode(string_components[1]),
        'height': base74_decode(string_components[2]),
        'data': string_components[3],
        'tutorial_text': string_components[4],
        'name': string_components[5],
    }

    decoded_data = decode_data(components['data'])
    placeables, cells = format_cells(decoded_data, components['width'], components['height'])

    level_data = {
        'size': (components['width'], components['height']),
        'placeables': placeables,
        'cells': cells,
        'tutorial_text': components['tutorial_text'],
        'name': components['name'],
    }

    lvl = Level(
        size=level_data['size'],
        cells=level_data['cells'],
        placeables=level_data['placeables'],
        name=level_data['name'],
        tutorial_text=level_data['tutorial_text'],
    )

    return lvl