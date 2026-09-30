import alchemy
import elements


def lead_to_gold() -> str:
    air = alchemy.create_air()
    streng = alchemy.potions.strength_potion()
    fire = elements.create_fire()
    return f"Recipe transmuting Lead to Gold: brew {
        air} and {streng} mixed with {fire}"
