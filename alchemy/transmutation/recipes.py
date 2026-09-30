from .. import potions
from elements import create_fire


def lead_to_gold() -> str:
    air = potions.alchemy.create_air()
    strength = potions.strength_potion()
    fire = create_fire()
    return f"Recipe transmuting Lead to Gold: brew '{
        air}' and '{strength}' mixed with '{fire}'"
