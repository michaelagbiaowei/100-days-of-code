student_scores = input("Enter student scores\n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max = None

for num in student_scores:
    if max is None or num > max:
        max = num
print(max)

# max = student_scores[0]

# for x in student_scores:
#     if x > max:
#         max = x
# print(max)

# min = student_scores[0]

# for x in student_scores:
#     if x < min:
#         min = x
# print(min)