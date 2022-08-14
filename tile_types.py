from typing import Tuple

import numpy as np # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint
        ("fg", "3B"),     # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# Tile struct used for staically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),    # True if this tile can be walked over
        ("transparent", np.bool), # True if this tile doesn't block FOV
        ("dark", graphic_dt),     # Graphics for when this tile is not in FOV.
    ]
)


def new_tile(
    *, # Enforce the use of keywords, so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

RGB_COLOR = {
    "WHITE_RGB": (255, 255, 255),
    "COLOR1_RGB": (50, 50, 150),
    "COLOR2_RGB": (0, 0, 100),
}


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), RGB_COLOR["WHITE_RGB"], RGB_COLOR["COLOR1_RGB"])
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), RGB_COLOR["WHITE_RGB"], RGB_COLOR["COLOR2_RGB"])
)