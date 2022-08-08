if __name__ == '__main__':
    
    records = []
    
    grades = []
    
    finNames = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        stdRecord = [name, score]
        
        records.append(stdRecord)
    
    for i in range(len(records)) :
        grades.append(records[i][1])
        
    grades.sort()
    
    for i in range(len(grades)):
        if i+1 > len(grades):
            break
        elif grades[i] < grades[i+1] :
            grades = float(grades[i+1])
            break
        else:
            continue
    
    for i in range(len(records)):
        if records[i][1] == grades:
           finNames.append(records[i][0])
    
    finNames.sort()
    
    for name in finNames :
        print(name)


# Input :
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

