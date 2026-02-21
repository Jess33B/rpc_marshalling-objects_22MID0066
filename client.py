from models import StudentProfile
from transport import send_request

if __name__ == "__main__":
    profile = StudentProfile(
        name="Jesna Binu Mancherikalam",
        id=1,
        grades=[98, 86, 95]
    )

    response = send_request(
        "calculate_grade_average",
        profile.to_dict()
    )

    print("Average:", response["result"])