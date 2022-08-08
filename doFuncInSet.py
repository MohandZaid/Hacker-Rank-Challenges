# num_element = int(input())
# elements = set(map(int,input().split()))

num_element = 9
elements = {1,2,3,4,5,6,7,8,9} 
num_command = 10

# for _ in range(int(input())):
for _ in range(num_command):
    command= input().strip()
    
    if command == 'pop':
        execute = f'elements.{command}()'
        eval(execute)
        continue
    
    command, num = command.split()
    num = int(num)
    
    execute = f'elements.{command}({num})'
    
    eval(execute)

print(sum(elements))

'''
#INPUT

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

'''
#Solution 2

# n = int(input())
# s = set(map(int, input().split())) 
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))

#Solution 3

# n = int(input())
# s = set(map(int, input().split())) 
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))

### Note ###
# s = {*[i for i in range(100)]}

# print(s)
# print(s.pop())

#Solution 4

# num_element = int(input())
# elements = set(map(int,input().split()))

# for _ in range(int(input())):
#     command= input().strip()
    
#     if command == 'pop':
#         elements.pop()
#         continue
    
#     command, num = command.split()
#     num = int(num)
    
#     if command == 'remove':
#         elements.remove(num)
        
#     elif command == 'discard':
#         elements.discard(num)
        
# print(sum(elements))
