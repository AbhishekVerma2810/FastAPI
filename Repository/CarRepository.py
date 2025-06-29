import json
from pathlib import Path

from Schema import Car, CarInput


class CarRepository:
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

    def get_all(self) -> list[Car]:
        return self._read()

    def add(self, car_input: CarInput) -> Car:
        cars = self.get_all()

        current_max_id = max([carObject.Id for carObject in cars])

        new_car = Car(Id = current_max_id + 1, **car_input.model_dump())
        cars.append(new_car)

        self._write(cars)
        return new_car

    def update(self, updated_car: Car) -> bool:
        cars = self.get_all()

        for idx, car in enumerate(cars):
            if car.Id == updated_car.Id:
                cars[idx] = updated_car
                break

        self._write(cars)
        return True

    def delete(self, car_to_delete: Car) -> bool:
        cars = self.get_all()
        cars.remove(car_to_delete)

        self._write(cars)
        return True