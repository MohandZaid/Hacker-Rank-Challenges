num_students, num_subjects = list(map(int,input().split()))

all_students = []

for subject in range(int(num_subjects)):
    all_degrees_of_subject = list(map(float,input().split()))
    all_students.append(all_degrees_of_subject) 

all_students = list(zip(*all_students))

for student in range(num_students):
    average = sum(all_students[student]) / num_subjects
    print(average)


'''
# INPUT 

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
'''