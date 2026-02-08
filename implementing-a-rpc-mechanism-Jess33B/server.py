from marshalling import validate_types

def calculate_grade_average(profile):
    # Validate incoming RPC data
    validate_types(profile)

    if len(profile.grades) == 0:
        return 0.0

    return sum(profile.grades) / len(profile.grades)
