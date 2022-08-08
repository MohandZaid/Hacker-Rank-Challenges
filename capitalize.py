def solve1(s):
    
    name = ''
    
    nameList = s.split(' ')
    
    for nameLoop in nameList :
        
        nameLoop = nameLoop.capitalize()
        name += nameLoop + ' ' 
    
    return name.strip()


def solve2(s):
    
    s = s.split(' ')
    
    for i in range(len(s)) :
        
        s[i] = s[i].capitalize()
    
    #s = ' '.join(s)

    return ' '.join(s) 


print(solve1(input()))
print(solve2(input()))

