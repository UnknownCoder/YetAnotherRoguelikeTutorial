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
        ("light", graphic_dt),    # Graphics for when this tile is in FOV
    ]
)


def new_tile(
    *, # Enforce the use of keywords, so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
WHITE_RGB  = (255, 255, 255)
BLACK_RGB  = (0, 0, 0)
GOLD_RGB   = (200, 180, 50)
CLAY_RGB   = (130, 110, 50)
PURPLE_RGB = (50, 50, 150)
BLUE_RGB   = (0, 0, 100)

SHROUD = np.array((ord(" "), WHITE_RGB, BLACK_RGB), dtype=graphic_dt)

floor = new_tile(
    walkable=True, 
    transparent=True,
    dark=(ord(" "), WHITE_RGB, PURPLE_RGB),
    light=(ord(" "), WHITE_RGB, GOLD_RGB),
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord(" "), WHITE_RGB, BLUE_RGB),
    light=(ord(" "), GOLD_RGB, CLAY_RGB),
)