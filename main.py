import random

def generate_seat_plan(students, rows, cols):
    """
    Generates a simple seat plan.

    Args:
        students: A list of student names.
        rows: Number of rows in the exam hall.
        cols: Number of columns in the exam hall.

    Returns:
        A 2D list representing the seat plan.
    """

    random.shuffle(students)  # Randomize student order

    seat_plan = [[None for _ in range(cols)] for _ in range(rows)]
    index = 0

    for i in range(rows):
        for j in range(cols):
            seat_plan[i][j] = students[index]
            index += 1

    return seat_plan

def print_seat_plan(seat_plan):
    """Prints the seat plan in a readable format."""

    for row in seat_plan:
        for seat in row:
            print(f"{seat:15}", end="")
        print()

# Example usage:
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"]
rows = 4
cols = 2

seat_plan = generate_seat_plan(students, rows, cols)
print_seat_plan(seat_plan)