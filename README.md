cellmachine [[source]](https://github.com/itskegnh/cellmachine/blob/master/src/cellmachine/__init__.py)
===========
<img src="https://img.shields.io/pypi/pyversions/cellmachine"></img> <img src="https://img.shields.io/pypi/v/cellmachine?color=blue"></img>

Key Features
------------
 - Import and export [these level codes](#supported-code-formats).
 - Read and modify levels with [these cells](#supported-cells).

Installation
------------
**[Python 3.7+](https://www.python.org/downloads/) is required**
```sh
# MacOS / Linux (via Terminal)
python3 -m pip install -U cellmachine

# Windows (via CMD Prompt)
py -3 -m pip install -U cellmachine
```

Quick Examples
--------------
```py
import cellmachine as cm
level = cm.Level.from_code("...")
print(level.name) # display the level's name attribute.
```

---
## BorderType
> A class that represents a border type.

| Attributes |
| ---------- |
| [Stop](#bordertype-stop-source) |
| [Wrap](#bordertype-wrap-source) |
| [Delete](#bordertype-delete-source) |
| [Flip](#bordertype-flip-source) |

---
### `BorderType` Stop [[source]]()
> Represents the 'Stop' border type. The border acts like a wall, Immovable.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

### `BorderType` Wrap [[source]]()
> Represents the 'Wrap' border type. The border acts like the corresponding cell on the other side of the level.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

### `BorderType` Delete [[source]]()
> Represents the 'Delete' border type. The border acts like a trash cell, any cells pushed into it are destroyed.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

### `BorderType` Flip [[source]]()
> Represents the 'Flip' border type. The border acts like a mirror, any cells pushed into it are flipped.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)
---
## Level

| Attributes | Methods | Subclasses |
| ---------- | ------- | - |
| [border](#level-border-source) | [from_code](#level-fromcode-source) | [LevelSize](#level-levelsize-source) |
| [name](#level-name-source) | |
| [text](#level-text-source) | |

---

### `Level` border [[source]]()
> The border type of the level.

**Type:**
 - [BorderType](#bordertype)

### `Level` name [[source]]()
> The name of the level. Shown in the level editor.

**Type:**
 - [str](https://docs.python.org/3/library/functions.html#func-str)

### `Level` text [[source]]()
> The text of the level. Text to appear while in play / editor mode.

**Type:**
 - [str](https://docs.python.org/3/library/functions.html#func-str)

---

### `Level` from_code [[source]]()
**Parameters:**
 - `code` (*[str](https://docs.python.org/3/library/functions.html#func-str)*) - The level code string. [Supported Formats](#supported-code-formats)

**Returns:**
 - `Level` (*[Level](#level)*)

---

### `Level` LevelSize [[source]]()
> A class to represent a level's size.

| Attributes |
| ---------- |
| [width](#levellevelsize-width-source) |
| [height](#levellevelsize-height-source) |
| [size](#levellevelsize-size-source) |
| [x](#levellevelsize-x-source) |
| [y](#levellevelsize-y-source) |
| [area](#levellevelsize-area-source) |

---

### `Level.LevelSize` width [[source]]()
> The width of the level.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

### `Level.LevelSize` height [[source]]()
> The height of the level.

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

### `Level.LevelSize` size [[source]]()
> The size of the level.

**Type:**
 - [tuple](https://docs.python.org/3/library/functions.html#func-tuple)

### `Level.LevelSize` x [[source]]()
> Alias for [width](#levellevelsize-width-source).

### `Level.LevelSize` y [[source]]()
> Alias for [height](#levellevelsize-height-source).

### `Level.LevelSize` area [[source]]()
> The area of the level. (width * height)

**Type:**
 - [int](https://docs.python.org/3/library/functions.html#int)

---

## Other

### Supported Code Formats
The currently supported codes are:
| Name | Remake | Latest | 
| - | - | - |
| V1 | [Mystic Mod](https://mystic-mod.com/) | ⛔️ |
| V2 | [Mystic Mod](https://mystic-mod.com/) | ⛔️ |
| V3 | [Mystic Mod](https://mystic-mod.com/) | ✅ |

---

### Supported Cells
| Texture | Name | Description | Mobile |
| - | - | - | - |
| <img src="./images/generator.png"></img> | Generator | Duplicates the cell behind it to the front, if the cell infront is empty or mobile. | ✅ |
| <img src="./images/CW_rotator.png"></img> | Clockwise Rotator | Rotates all neighbour cells clockwise that are mobile. | ✅ |
| <img src="./images/CCW_rotator.png"></img> | Counter-clockwise Rotator | Rotates all neighbour cells counter-clockwise that are mobile. | ✅ |
| <img src="./images/mover.png"></img> | Mover | Moves in the direction its facing, pushes mobile cells. | ✅ |
| <img src="./images/slide.png"></img> | Slide | Is only mobile in the direction of the parrallel lines. | ❎ |
| <img src="./images/push.png"></img> | Push | Mobile in all directions. | ✅ |
| <img src="./images/wall.png"></img> | Wall | Immobile in all directions. Cannot be rotated. | ⛔️ |
| <img src="./images/enemy.png"></img> | Enemy | When a cell is moved into the same location as an enemy cell, both cells will be destroyed. | ⛔️ |
| <img src="./images/trash.png"></img> | Trash | Destroys any cell pushed into it. | ⛔️ |
| <img src="./images/0.png"></img> | Placeable | The only "cell" which can share a space with another cell. Only cells marked with this can be moved in 'Play' mode. | ⛔️ |
---