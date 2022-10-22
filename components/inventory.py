from __future__ import annotations
from lib2to3.pytree import Base

from typing import List, TYPE_CHECKING

from base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __in