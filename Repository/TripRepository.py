import json
from pathlib import Path
from Repository.CarRepository import CarRepository
from Schema.Car import Car
from Schema.Trip import Trip, TripInput


class TripRepository:
    def __init__(self, file_path: str | None = None):
        self.jsonFilePath = "Cars.json"

        if file_path:
            self.jsonFilePath = file_path

        if not Path(self.jsonFilePath).exists():
            with open(self.jsonFilePath, 'w') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def _read(self) -> list[Car]:
        with open(self.jsonFilePath, 'r') as f:
            return [Car.model_validate(carDict) for carDict in json.load(f)]

    def _write(self, data: list[Car]):
        with open(self.jsonFilePath, 'w') as f:
            json.dump([Car.model_dump(car) for car in data], f, indent=4)

    def add(self, car_id: int, trip_input: TripInput) -> Trip:
        cars = CarRepository().get_all()

        for car in cars:
            if car.Id == car_id:
                current_max_id = max([tripObject.Id for tripObject in car.Trips], default = 0)

                new_trip = Trip(Id = current_max_id + 1, **trip_input.model_dump())
                car.Trips.append(new_trip)

                self._write(cars)
                return new_trip

    def update(self,car_id: int, updated_trip: Trip) -> bool:
        cars = CarRepository().get_all()

        for car_idx, car in enumerate(cars):
            if car.Id == car_id:
                for trip_idx, trip in enumerate(car.Trips):
                    if trip.Id == updated_trip.Id:
                        car.Trips[trip_idx] = updated_trip
                        break

        self._write(cars)
        return True

    def delete(self, car_id: int, trip_to_delete: Trip) -> bool:
        cars = CarRepository().get_all()
        for car in cars:
            if car.Id == car_id:
                car.Trips.remove(trip_to_delete)

        self._write(cars)
        return True