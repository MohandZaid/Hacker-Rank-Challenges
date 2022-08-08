def swap_case(s):
    newS = ''
    
    for char in s :
        if char.isupper() : newS += char.lower() 
        
        elif char.islower() : newS += char.upper() 
        
        else :
            newS += char
        
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)