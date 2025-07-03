from dataclasses import field
from typing import Optional
from pydantic import BaseModel
from Schema.Enums import TransmissionEnum, FuelEnum, SizeEnum
from Schema.Trip import Trip


class CarInput(BaseModel):
    CarName: str
    CarManufacturer: str
    MakeYear: int
    TransmissionType: Optional[TransmissionEnum] = TransmissionEnum.Manual
    FuelType: Optional[FuelEnum] = FuelEnum.Petrol
    Size: Optional[SizeEnum] = SizeEnum.S

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "CarName": "Dzire",
                    "CarManufacturer": "Maruti",
                    "MakeYear": 2024,
                    "TransmissionType": "Manual",
                    "FuelType": "Petrol",
                    "Size": "S"
                }
            ]
        }
    }

class Car(CarInput):
    Id: int
    Trips: list[Trip] = field(default_factory=list)