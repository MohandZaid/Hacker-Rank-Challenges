# names = ['mohand','abdelaleem','zaid']
# mapednames = map(print,names)

# print(mapednames)

# for name in mapednames:
#     continue



# names = ['mohand','abdelaleem','zaid']
# mapednames = map(print,names)

# mapednames = list(mapednames)
# print(mapednames)
# for name in mapednames:
#     pass

names = ['mohand','abdelaleem','zaid']
mapednames = map(lambda x:f'-{x.upper()}-',names)

print(mapednames)

for name in mapednames:
    print(name)
    
    
# names = ['mohand','abdelaleem','zaid']
# mapednames = map(lambda x:f'-{x.upper()}-',names)

# mapednames = list(mapednames)
# print(mapednames)

# for name in mapednames:
#     print(name)
