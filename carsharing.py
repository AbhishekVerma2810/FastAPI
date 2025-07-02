import uvicorn
from fastapi import FastAPI, HTTPException
from Repository.CarRepository import CarRepository
from Repository.TripRepository import TripRepository
from Schema.Car import Car
from Schema.Car import CarInput
from typing import Optional
from Schema.Trip import TripInput, Trip


app = FastAPI(title="Car Sharing")
carRepo = CarRepository()
tripRepo = TripRepository()
cars = carRepo.get_all()

@app.get("/")
def welcome() -> str:
    """Return a friendly welcome message"""
    return "Welcome to the Car Sharing service!"

@app.get("/api/cars")
def get_cars(size: Optional[str] = None, make_year: Optional[int] = None) -> list[Car]:
    """Get all available cars"""
    result = carRepo.get_all()
    if size:
        result = [car for car in result if car.Size == size]
    if make_year:
        result = [car for car in result if car.MakeYear >= make_year]
    return result

@app.get("/api/cars/{car_id}")
def get_car_by_id(car_id: int) -> Car:
    for car in carRepo.get_all():
        if car.Id == car_id:
            return car

    raise HTTPException(status_code=404, detail=f"No car with id={car_id}")

@app.post("/api/cars", status_code=201)
def add_car(car: CarInput) -> Car:
    new_car = carRepo.add(car)
    return new_car

@app.put("/api/cars/{car_id}", status_code=200)
def change_car(car_id: int, new_data: CarInput) -> Car:
    car = get_car_by_id(car_id)

    car.Size = new_data.Size
    car.MakeYear = new_data.MakeYear
    car.CarName = new_data.CarName
    car.CarManufacturer = new_data.CarManufacturer
    car.FuelType = new_data.FuelType
    car.TransmissionType = new_data.TransmissionType

    carRepo.update(car)

    return car

@app.delete("/api/cars/{car_id}", status_code=204)
def delete_car(car_id: int):
    car = get_car_by_id(car_id)
    carRepo.delete(car)

@app.get("/api/cars/{car_id}/trips", status_code=200)
def get_trips(car_id: int) -> list[Trip]:
    car = get_car_by_id(car_id)
    return car.Trips

@app.get("/api/cars/{car_id}/trips/{trip_id}", status_code=200)
def get_trip_by_id(car_id: int, trip_id: int) -> Trip:
    car = get_car_by_id(car_id)

    for trip in car.Trips:
        if trip.Id == trip_id:
            return trip

    raise HTTPException(status_code=404, detail=f"No trip with id={trip_id} for car with id={car_id}")

@app.post("/api/cars/{car_id}/trips", status_code=201)
def add_trip(car_id: int, trip: TripInput) -> Trip:
    new_trip = tripRepo.add(car_id, trip)
    return new_trip

@app.put("/api/cars/{car_id}/trips/{trip_id}", status_code=200)
def change_trip(car_id: int, trip_id: int, new_data: TripInput) -> Trip:
    trip = get_trip_by_id(car_id, trip_id)

    trip.Start = new_data.Start
    trip.End = new_data.End
    trip.Description = new_data.Description
    tripRepo.update(trip)

    return trip
    
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)