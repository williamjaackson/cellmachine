"""
import cellmachine as cm
level = cm.Level.from_code("V1;20;20;...;...;name;0")

"""

from enum import Enum
import re


class BorderType(Enum):
    """
    A class to represent a border type.

    Attributes
    ----------
    Stop : BorderType
        The border acts like a wall, Immovable.
    Wrap : BorderType
        The border acts like the corresponding cell on the other side of the level.
    Delete : BorderType
        The border acts like a trash cell, all cells pushed into it are deleted.
    Flip : BorderType
        The border acts like a mirror, all cells pushed into it are flipped.
    """

    Stop = 0
    Wrap = 1
    Delete = 2
    Flip = 3


class Level:
    """
    A class to represent a level.

    Attributes
    ----------
    border : BorderType
        The border type of the level.
    size : Level.LevelSize
        The size of the level.
    name : str or NoneType
        The level's name (unused in-game).
    text : str or NoneType
        Text to appear while in play / editor mode.

    """

    def __init__(self):
        self.border = BorderType.Stop
        self.size = Level.LevelSize(0, 0)
        self.name, self.text = None, None

    class LevelSize:
        """
        A class to represent a level's size.

        Attributes
        ----------
        width : int
            The level's width.
        height : int
            The level's height.
        size : tuple
            The level's size.
        x : int
            an alias for width.
        y : int
            an alias for height.
        area : int
            the total area of the level.
        """

        def __init__(self, width, height):
            """
            The constructor for the LevelSize class.

            Parameters
            ----------
            width : int
                The level's width.
            height : int
                The level's height.
            """
            self.width = width
            self.height = height

        size = property(
            lambda self: (self.width, self.height),
            lambda self, value: (
                setattr(self, "width", value[0]),
                setattr(self, "height", value[1]),
                None,
            )[-1],
        )

        x = property(
            lambda self: self.width, lambda self, value: setattr(self, "width", value)
        )

        y = property(
            lambda self: self.height, lambda self, value: setattr(self, "height", value)
        )

        area = property(lambda self: self.width * self.height)

    @classmethod
    def from_code(cls, code):
        """
        Returns a Level object from a level code string.

        Parameters
        ----------
            code : str
                The level code string.
                Supported level_codes include: V1, V2, V3.

        Returns
        -------
            Level
                A Level object created from the level code string.
        """
        level = cls()

        # level code is V1
        # format: V1;<size x>;<size y>;<placeables=[<x>.<y>]>;<cells=[<type>.<rot>.<x>.<y>]>;Text;<border-type>
        # regex: V1;\d+;\d+;(\d+\.\d+,)*(\d+\.\d+){0,1};(\d+\.[0123]+\.\d+\.\d+,)*(\d+\.[0123]+\.\d+\.\d+){0,1};(.)*;(.)
        if re.match(
            r"^V1;\d+;\d+;(\d\.\d,?)*;([0-8]\.[0-3]\.\d+\.\d+,?)*;[\w\d]*;[0-3]?$",
            code,
        ):
            # x, y, placeables, cells, text, border ; missing and unused in-game: name
            level_list = code.split(";")

            level.size.size = (int(level_list[1]), int(level_list[2]))
            level.text = level_list[5]
            try:
                level.border = BorderType(int(level_list[6]))
            except ValueError:
                level.border = BorderType.Stop

            for placeable in level_list[3].split(","):
                x, y = placeable.split(".")
                # TODO: implement placeable

            for cell in level_list[4].split(","):
                type, rotation, x, y = cell.split(".")
                # TODO: implement cells
        # level code is V2
        # format: V2;<size x>;<size y>;<cells/placeables=base 74 mapping>;Text;Name;<border-type>
        elif re.match(
            r"^V2;[\da-zA-Z!$%&+-.=?^{}]+;[\da-zA-Z!$%&+-.=?^{}]+;[\da-zA-Z!$%&+-.=?^{}()]*;[\w\d]*;[\w\d]*;[0-3]?$",
            code,
        ):
            # x, y, cells/placeables, text, name (unused in-game), border
            level_list = code.split(";")

            # level.size.size = (b74_decode(level_list[1]), b74_decode(level_list[2]))
            level.text = level_list[4]
            level.name = level_list[5]
            try:
                level.border = BorderType(int(level_list[6]))
            except ValueError:
                level.border = BorderType.Stop

            if level_list[3] != "":
                level_list[3] += "0"  # To not error when checking for ) or (

                # count = pos = 0
                # while count < len(level_list[3]) - 1:
                #     if level_list[3][count + 1] == ")":
                #         repeat = b74_decode(level_list[3][count + 2]) + 1
                #         count_add = 3
                #     elif level_list[3][count + 1] == "(":
                #         repeat = b74_decode(level_list[3][count + 2 :].split(")")[0]) + 1
                #         count_add = 3 + len(level_list[3][count + 2 :].split(")")[0])
                #     else:
                #         repeat = 1
                #         count_add = 1

                #     cell_num = b74_decode(level_list[3][count])
                #     for i in range(repeat):
                #         if cell_num > 71:
                #             level[(pos + i) % width, (pos + i) // height] = cell_num % 2 == 1
                # TODO: create a way to set cells/placeables in the level
                #         else:
                #             level[(pos + i) % width, (pos + i) // height] = (
                #                 Cell(cell_num // 2 % 9, cell_num // 18 % 4),
                #                 cell_num % 2 == 1,
                #             )

                #     count += count_add
                #     pos += repeat
            # TODO: implement b74_decode
        else:
            raise ValueError("Invalid level code.")
            # TODO: raise custom error when level code is invalid

        return level


if __name__ == "__main__":
    # help(Level)
    level = Level.from_code(
        "V1;100;100;25.44,25.45,27.46,29.48,31.50,32.50,48.50,49.50,34.51,35.51,37.51,39.51,41.51,43.51,44.51,46.51,47.51;1.0.67.37,1.0.68.37,1.0.69.37,1.0.70.37,1.0.65.38,1.0.70.38,1.0.61.39,1.0.62.39,1.0.60.40,1.0.70.40,1.0.48.41,1.0.60.41,1.0.71.41,1.0.48.42,1.0.59.42,1.0.50.43,1.0.53.43,1.0.56.43,1.0.58.43,1.0.59.43;Text;0"
    )
