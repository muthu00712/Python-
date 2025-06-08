n = int(input())
MAX_CAPACITY = 30
student_db = {}
is_full = False
for _ in range(n):
 parts = input().split()
 student_id = int(parts[0])
 student_name = parts[1]
 if is_full:
  continue
 if len(student_db) >= MAX_CAPACITY:
  print("Exception caught. Error: Student database is full.")
  is_full = True
 elif student_id in student_db:
  print("Exception caught. Error: Student ID already exists.")
 else:
  student_db[student_id] = student_name
  print(f"Student with ID {student_id} added to the database.")