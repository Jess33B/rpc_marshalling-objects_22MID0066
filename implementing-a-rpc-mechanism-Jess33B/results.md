# Lab DA-1 Results

## RPC Method
calculate_grade_average(StudentProfile profile)

## Valid Input Test
Input:
- name: Jess
- id: 1
- grades: [70, 80, 90]

Output:
- Average: 80.0

## Invalid Input Test
Input:
- id provided as string
- grades containing non-integer values

Result:
- TypeError raised on server side as expected

## Conclusion
The marshalling layer successfully validates incoming RPC data and prevents invalid remote procedure execution.
