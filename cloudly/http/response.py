from dataclasses import dataclass
import json
from typing import Any, Callable
from flowfast.step import Task, Mapping


def HttpResponse(status_code=200, data: dict = None):
    return {
        "statusCode": status_code,
        "Content-Type": "application/json",
        "body": json.dumps(data) if data else "",
    }


@dataclass
class RespondWith(Task):
    status: int = 200
    data_shaper: Callable[[Mapping], Any] = None

    def process(self, input: Mapping) -> Mapping:
        response_data = self.data_shaper(input) if self.data_shaper else input
        return HttpResponse(self.status, response_data)
