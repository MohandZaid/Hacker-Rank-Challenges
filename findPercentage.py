if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input().strip()
    
    avg = lambda a,b,c : ((a+b+c)/3)       
            
    print('{:.2f}'.format(avg(student_marks[query_name][0] 
    ,student_marks[query_name][1] ,
    student_marks[query_name][2])))

# Input Example:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika