# Grade book starts with a variable from last year, this houses a list containing (subject, grade)
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Create a new list of classes for this year
subjects = ["physics", "calculus", "poetry", "history"]
# Create a new list of grades for this year, in order of classes
grades = [98, 97, 85, 88]

# Add a new class to list "subjects" you just finished called "computer science"
subjects.append("computer science")
# Add a new grade to list "grades" with a score of 100
grades.append(100)

# Combine lists "subjects" and "grades" into a new list called "gradebook"
gradebook = zip(subjects, grades)

print(list(gradebook))  # Print to confirm output, specify you want to output as a list otherwise its unreadable.

# Combine this years list "gradebook" with last years list "last_semester_gradebook"
full_gradebook = list(gradebook) + list(last_semester_gradebook)

print(list(full_gradebook))  # Print to confirm output, specify you want to output as a list otherwise its unreadable
