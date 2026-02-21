from dataclasses import dataclass
from typing import List

@dataclass
class StudentProfile:
    name: str
    id: int
    grades: List[int]

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data: dict):
        return StudentProfile(
            name=data["name"],
            id=data["id"],
            grades=data["grades"]
        )