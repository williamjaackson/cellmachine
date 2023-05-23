from . import v1, v2, v3


def import_level(level_string):
    string_components = level_string.split(";")

    if string_components[0] == 'V1':
        return v1.import_level(level_string)
    elif string_components[0] == 'V2':
        return v2.import_level(level_string)
    elif string_components[0] == 'V3':
        return v3.import_level(level_string)
    else:
        raise ValueError("Invalid level version")