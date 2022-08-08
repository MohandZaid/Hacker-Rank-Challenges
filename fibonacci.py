cube = lambda x: pow(x,3) 

def fibonacci(n):
    outList = []
    for counter in range(n):
        if counter < 2 : 
            outList.append(counter)
        else :
            outList.append(outList[-1]+outList[-2])
    return outList

if __name__ == '__main__':
    # n = int(input())
    n = 11
    print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))