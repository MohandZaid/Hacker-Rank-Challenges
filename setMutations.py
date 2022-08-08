'''
# Making Operation With Update

hacker = {'h', 'a', 'c', 'k', 'e', 'r'}
rank = {'r', 'a', 'n', 'k'}

hacker.update(rank)
# hacker |= rank
print(hacker)

hacker.intersection_update(rank)
# hacker &= rank
print(hacker)

hacker.difference_update(rank)
# hacker -= rank
print(hacker)

hacker.symmetric_difference_update(rank)
# hacker ^= rank
print(hacker)

'''

num, elements = int(input()), set(map(int,input().split()))

for _ in range(int(input())):
    
    operation, length = input().split()
    op_set = set(map(int, input().split()))
    
    eval(f'elements.{operation}({op_set})')
    
print(sum(elements))

'''
# INPUT
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

'''
