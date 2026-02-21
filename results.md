# Lab DA-1: RPC Framework with Object Marshalling

## Objective
Implemented a Remote Procedure Call (RPC) framework in Python
to remotely invoke:

    float calculate_grade_average(StudentProfile profile)

## Implementation Details
input was-name="Jesna Binu Mancherikalam",
        id=1,
        grades=[98, 86, 95]

### StudentProfile Object
Contains:
- name (string)
- id (integer)
- grades (list of integers)

### Marshalling Layer
The marshalling layer:
- Serializes objects into JSON
- Validates incoming data using validate_types()
- Raises TypeError if incorrect data types are received

### Type Validation
The validate_types() function checks:
- name is string
- id is integer
- grades is list
- each grade is integer

If any mismatch occurs, a TypeError is raised.

### RPC Workflow
Client → JSON serialization → Transport → Server → Validation → Execution → JSON Response

### Example Output
Average: 80.0

## Conclusion
Successfully implemented RPC with:
- Object marshalling
- Server-side validation
- Clean architecture
- Error handling