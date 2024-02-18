# Split a string of student grades into a list and an array of integers
from array import array

grades_data = "90 85 92 78 88"

# Using split() to separate individual grades and map them to integers
grades_list = list(map(int, grades_data.split()))

# Using split() and array() to create an array of grades
grades_array = array('i', map(int, grades_data.split()))

print("After splitting the string of student grades:")
print("List of Grades:", grades_list)
print("Array of Grades:", grades_array)
