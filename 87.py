def dui_bi(n):
    score = -1; student = str()
    for i in range(n):
        student_info = input().split()
        if int(student_info[2]) + int(student_info[3]) +int(student_info[4]) > score:
            score = int(student_info[2]) + int(student_info[3]) +int(student_info[4])
            student = student_info[1] + ' ' + student_info[0] + ' ' + str(score)
    return student
print(dui_bi(int(input())))