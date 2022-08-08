M_size = int(input())
M_set = set(map(int,input().split()))

N_size = int(input())
N_set = set(map(int,input().split()))

sym_diff = set()
sym_diff.update(M_set.difference(N_set), N_set.difference(M_set))
sym_diff = list(sym_diff)
sym_diff.sort()

for i in sym_diff:
    print(i)

'''
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
'''