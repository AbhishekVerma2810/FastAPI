from enum import Enum


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