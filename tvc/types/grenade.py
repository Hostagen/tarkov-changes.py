from typing import TypedDict

from .cell import Cell
from .item import ItemBase

_Grenade = TypedDict(
    '_Grenade',
    {
        'Can Be Hidden During Throw': str,
        'Contusion Distance': str,
        'Explosion Delay': str,
        'Fragments Count': str,
        'Max Explosion Distance': str,
        'Min Explosion Distance': str,
        'Strength': str,
        'Item Weight': str,
        'Can be sold on flea market': str,
        'Max Stack Size': str,
        'Discard Limit': str,
    },
    total=False,
)


class Grenade(_Grenade, ItemBase, Cell):
    pass
