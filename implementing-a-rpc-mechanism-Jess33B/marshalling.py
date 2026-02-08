def validate_types(profile):
    if not isinstance(profile.name, str):
        raise TypeError("name must be a string")

    if not isinstance(profile.id, int):
        raise TypeError("id must be an integer")

    if not isinstance(profile.grades, list):
        raise TypeError("grades must be a list")

    for grade in profile.grades:
        if not isinstance(grade, int):
            raise TypeError("each grade must be an integer")
