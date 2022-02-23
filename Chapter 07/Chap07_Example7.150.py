from collections import defaultdict

student_subject_marks = [
    ('Maths', 90),
    ('Physics', 92),
    ('Chemistry', 80),
    ('Biology', 80),
    ('English', 80),
    ('Maths', 90)
]

my_chars = defaultdict(list)

for mykey, myvalue in student_subject_marks:
    my_chars[mykey].append(myvalue)

print(list(my_chars.items()))