# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
x,y,z,n = 1,1,1,2

cube = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n]
 
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             cube.append([i,j,k])
        
# cube = [i for i in cube if sum(i) != n ]

print(cube)
