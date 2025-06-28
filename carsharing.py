import uvicorn
from fastapi import FastAPI, HTTPException

from Repository.CarRepository import CarRepository

app = FastAPI()
cars = CarRepository().getAll()

@app.get("/")
def welcome() -> str:
    """Return a friendly welcome message"""
    return "Welcome to the Car Sharing service!"

@app.get("/api/cars")
def get_cars(size: str|None = None, make_year: int|None = None) -> list[dict]:
    """Get all available cars"""
    result = cars
    if size:
        result = [car for car in cars if car.Size == size]
    if make_year:
        result = [car for car in cars if car.MakeYear >= make_year]
    return result

@app.get("/api/cars/{id}")
def get_car_by_id(id: int) -> dict:
    for car in cars:
        if car.Id == id:
            return car

    raise HTTPException(status_code=404, detail=f"No car with id={id}")

# if __name__ == "__main__":
#     uvicorn.run("carsharing:app", reload=True)