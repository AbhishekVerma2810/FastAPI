from enum import Enum
from typing import Optional

from pydantic import BaseModel

class SizeEnum(str, Enum):
    S = "S"
    M = "M"
    L = "L"

class FuelEnum(str, Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    CNG = "CNG"
    Electric = "Electric"

class TransmissionEnum(str, Enum):
    Manual = "Manual"
    Automatic = "Automatic"

class CarInput(BaseModel):
    CarName: str
    CarManufacturer: str
    MakeYear: int
    TransmissionType: Optional[TransmissionEnum] = TransmissionEnum.Manual
    FuelType: Optional[FuelEnum] = FuelEnum.Petrol
    Size: Optional[SizeEnum] = SizeEnum.S

class Car(CarInput):
    Id: int