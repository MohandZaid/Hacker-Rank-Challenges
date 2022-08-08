# set_EN = set(map(int,input().split()))
# set_FR = set(map(int,input().split()))

set_EN = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_FR = {10, 1, 2, 3, 11, 21, 55, 6, 8}

print(set_EN.union(set_FR))
print(set_EN | set_FR)

print(set_EN.intersection(set_FR))
print(set_EN & set_FR)

print(set_EN.difference(set_FR))
print(set_EN - set_FR)

print(set_FR.difference(set_EN))
print(set_FR - set_EN)

print(set_EN.symmetric_difference(set_FR))
print(set_EN ^ set_FR)

print(dir(set))