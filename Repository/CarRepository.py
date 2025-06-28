import json
from pathlib import Path

from Schema import Car


class CarRepository:
    def __init__(self, filePath: str|None = None):
        self.jsonFilePath = "Cars.json"

        if filePath:
            self.jsonFilePath = filePath

        if not Path(self.jsonFilePath).exists():
            with open(self.jsonFilePath, 'w') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def _read(self):
        with open(self.jsonFilePath, 'r') as f:
            return [Car.model_validate(carDict) for carDict in json.load(f)]

    def _write(self, data):
        with open(self.jsonFilePath, 'w') as f:
            json.dump(data, f, indent=4)

    def getAll(self):
        return self._read()