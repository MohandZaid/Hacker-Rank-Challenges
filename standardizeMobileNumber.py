def wrapper(func):
    def inner(l):
        
        prfx = '+91'
        for i in range(len(l)) :
            if len(l[i]) > 10 :
                l[i] = l[i][len(l[i])-10 : ]
            
            l[i] = f'{prfx} {l[i][:5]} {l[i][5:]}'
            
        func(l)
        
    return inner

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


"""
Input:
3
07895462130
919875641230
9195969878

"""