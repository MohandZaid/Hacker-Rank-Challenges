# My Solving

def rev(string):
    string = list(string) 
    string.reverse()
    return string

def joinChar(string, newChar, status):
    string = list(string)
    
    if status :
        string.pop()
        string.pop()
        
    stringBuff = string.copy()
    string.append(newChar)
    string.extend(rev(stringBuff))
    string = '-'.join(string)
    return string

def print_rangoli(size):
    
    char = ['flag' ,'a','b','c','d','e','f',
            'g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v',
            'w','x','y','z']
    
    width = size * 2 - 1 + size * 2 - 2
    
    buff = ''
    status = False
    
    for index in range(size,0,-1):
        
        print(joinChar(buff,char[index],status).center(width,'-'))
        buff += char[index]
        
    status = True
    
    for index in range(2,size+1):
        
        print(joinChar(buff,char[index],status).center(width,'-'))
        buff = buff[:-1]
    
# Another Solving

# def print_rangoli(size):
#     for n in [abs(r) for r in range( -(size-1), size)]:
#         center='-'.join([ chr(ord('a')+abs(i)+n) for i in range(-(size-n-1), (size-n))])
#         print(2*n*'-' + center + 2*n*'-')

# Another Solving

# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#     for i in range(size-1):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))


if __name__ == '__main__':
    # n = int(input())

    n = 11

    print_rangoli(n)