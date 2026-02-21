def validate_types(data: dict):

    if not isinstance(data.get("name"), str):
        raise TypeError("name must be a string")

    if not isinstance(data.get("id"), int):
        raise TypeError("id must be an integer")

    if not isinstance(data.get("grades"), list):
        raise TypeError("grades must be a list")

    for grade in data["grades"]:
        if not isinstance(grade, int):
            raise TypeError("each grade must be an integer")