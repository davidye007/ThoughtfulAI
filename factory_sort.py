from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt
from typing import Union

# ---- Constants ----
BULKY_VOL_CM3 = 1000000
BULKY_DIM_CM = 150
HEAVY_KG = 20

class Package(BaseModel):
    """
    Represents a physical package for dispatch classification.
    Each package has three dimensions (in centimeters) and a mass (in kilograms).
    All measurements must be non-negative.
    """
    width: Union[NonNegativeInt, NonNegativeFloat]
    height: Union[NonNegativeInt, NonNegativeFloat]
    length: Union[NonNegativeInt, NonNegativeFloat]
    mass: Union[NonNegativeInt, NonNegativeFloat]


def sort(width, height, length, mass) -> str:
    """
    Determines the dispatch stack for a package.

    Args:
        width:   Width in centimeters
        height:  Height in centimeters
        length:  Length in centimeters
        mass:    Mass in kilograms

    Returns:
        One of "STANDARD", "SPECIAL", or "REJECTED" based on factory criteria.
    """
    package = Package(width=width, height=height, length=length, mass=mass)
    bulky = (package.width * package.height * package.length > BULKY_VOL_CM3
             or max(package.width, package.height, package.length) >= BULKY_DIM_CM)
    heavy = package.mass >= HEAVY_KG
    if not bulky and not heavy:
        return "STANDARD"
    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL"
