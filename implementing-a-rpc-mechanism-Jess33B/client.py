from models import StudentProfile
from server import calculate_grade_average

profile = StudentProfile(
    name="Jess",
    id=1,
    grades=[70, 80, 90]
)

result = calculate_grade_average(profile)
print("Average:", result)
