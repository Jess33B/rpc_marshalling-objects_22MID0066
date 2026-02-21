from __future__ import annotations
import json
from models import StudentProfile as StudentProfile
from marshalling import validate_types


def calculate_grade_average(profile: "StudentProfile") -> float:
    if len(profile.grades) == 0:
        return 0.0
    return sum(profile.grades) / len(profile.grades)


def handle_request(request_json: str) -> str:

    request = json.loads(request_json)

    function_name = request["function"]
    payload = request["payload"]

    validate_types(payload)

    profile = StudentProfile.from_dict(payload)

    if function_name == "calculate_grade_average":
        result = calculate_grade_average(profile)
    else:
        raise ValueError("Unknown RPC function")

    return json.dumps({"result": result})