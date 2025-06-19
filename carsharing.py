import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()
cars = [
    {"Id": 1, "CarName": "Swift", "CarManufacturer": "Maruti", "MakeYear": 2022, "TransmissionType": "Manual", "FuelType": "Petrol", "Size": "S"},
    {"Id": 2, "CarName": "Creta", "CarManufacturer": "Hyundai", "MakeYear": 2023, "TransmissionType": "Automatic", "FuelType": "Diesel", "Size": "M"},
    {"Id": 3, "CarName": "Fortuner", "CarManufacturer": "Toyota", "MakeYear": 2021, "TransmissionType": "Manual", "FuelType": "Diesel", "Size": "L"},
    {"Id": 4, "CarName": "Baleno", "CarManufacturer": "Maruti", "MakeYear": 2022, "TransmissionType": "Automatic", "FuelType": "Petrol", "Size": "M"},
    {"Id": 5, "CarName": "Nexon", "CarManufacturer": "Tata", "MakeYear": 2024, "TransmissionType": "Manual", "FuelType": "Electric", "Size": "M"},
    {"Id": 6, "CarName": "Seltos", "CarManufacturer": "Kia", "MakeYear": 2023, "TransmissionType": "Automatic", "FuelType": "Petrol", "Size": "M"},
    {"Id": 7, "CarName": "Alto", "CarManufacturer": "Maruti", "MakeYear": 2020, "TransmissionType": "Manual", "FuelType": "CNG", "Size": "S"},
    {"Id": 8, "CarName": "XUV700", "CarManufacturer": "Mahindra", "MakeYear": 2023, "TransmissionType": "Automatic", "FuelType": "Diesel", "Size": "L"},
    {"Id": 9, "CarName": "Tiago", "CarManufacturer": "Tata", "MakeYear": 2021, "TransmissionType": "Manual", "FuelType": "Petrol", "Size": "S"},
    {"Id": 10, "CarName": "Kiger", "CarManufacturer": "Renault", "MakeYear": 2022, "TransmissionType": "Automatic", "FuelType": "Petrol", "Size": "M"}
]

@app.get("/")
def welcome() -> str:
    """Return a friendly welcome message"""
    return "Welcome to the Car Sharing service!"

@app.get("/api/cars")
def get_cars(size: str|None = None, make_year: int|None = None) -> list[dict]:
    """Get all available cars"""
    result = cars
    if size:
        result = [car for car in cars if car['Size'] == size]
    if make_year:
        result = [car for car in cars if car['MakeYear'] >= make_year]
    return result

@app.get("/api/cars/{id}")
def get_car_by_id(id: int) -> dict:
    for car in cars:
        if car['Id'] == id:
            return car

    raise HTTPException(status_code=404, detail=f"No car with id={id}")

# if __name__ == "__main__":
#     uvicorn.run("carsharing:app", reload=True)