from collections import Counter

student_subject_marks = [
    ('Maths', 90),
    ('Physics', 92),
    ('Chemistry', 80),
    ('Biology', 80),
    ('English', 80),
    ('Maths', 90)
]

mycount = Counter(subjectname for subjectname, marks in student_subject_marks)
print(mycount)
