from pydantic import BaseModel

class Car(BaseModel):
    Id: int
    CarName: str
    CarManufacturer: str
    MakeYear: int
    TransmissionType: str|None = "Manual"
    FuelType: str|None = "Petrol"
    Size: str|None = "S"