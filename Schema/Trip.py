from pydantic import BaseModel


class TripInput(BaseModel):
    Start: int
    End: int
    Description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Start": 1013,
                    "End": 1458,
                    "Description": "Trip from New Delhi to Kanpur"
                }
            ]
        }
    }

class Trip(TripInput):
    Id: int