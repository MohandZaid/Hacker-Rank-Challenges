if __name__ == '__main__':

    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    for i in range(len(arr)):
        
        if i+1 > len(arr) :
            break
        
        elif arr[i] > arr[i+1]:
            print(arr[i+1])
            break
        
        else:
            continue

# Input :
# 5
# 2 3 6 6 5