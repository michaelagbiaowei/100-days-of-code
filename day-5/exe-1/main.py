student_height = input("Input a list of student heights\n").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    print(n)

# print(student_height)
count = 0
total = 0

for num in student_height:
    total += num
    count += 1
average = total / count 
print(round(average))