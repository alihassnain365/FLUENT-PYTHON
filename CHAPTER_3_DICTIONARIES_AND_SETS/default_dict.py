from collections import defaultdict

# words = ["python", "java", "python", "c++", "java", "python"]

# count = defaultdict(int)

# for word in words:
#     count[word] +=1

# print(count)


"""group students by Grade"""

# students = [
#     ("Ali", "A"),
#     ("Sara", "B"),
#     ("Ahmed", "A"),
#     ("Fatima", "C"),
#     ("Usman", "B")
# ]

# std_group = defaultdict(list)
# for student,grade in students:
#     std_group[grade].append(student)

# print(std_group)

     

""" Now finding the index position"""

# text = 'banana'

# char_pos = defaultdict(list)

# for i in range(len(text)):
#     char_pos[text[i]].append(i)

# print(char_pos)


""" final exercise"""

attendance = [
    ("Monday", "Ali"),
    ("Monday", "Sara"),
    ("Monday", "Ahmed"),
    ("Tuesday", "Ali"),
    ("Tuesday", "Fatima"),
    ("Wednesday", "Sara"),
    ("Wednesday", "Ali"),
    ("Thursday", "Ahmed"),
    ("Thursday", "Ali"),
    ("Friday", "Fatima"),
    ("Friday", "Sara"),
]

"""Create a dictionary where 
    each student maps to the 
    list of days they attended."""

std_filter_days = defaultdict(list)

for day,student in attendance:
    std_filter_days[student].append(day)

print(std_filter_days)


"""Create another dictionary where each day maps to the students who attended."""

std_filter_students = defaultdict(list)

for day,student in attendance:
    std_filter_students[student].append(day)

print(std_filter_students)


"""Count how many days each student attended."""

days_count = defaultdict(int)

for day,student in attendance:
    days_count[student] +=1

print(days_count)


