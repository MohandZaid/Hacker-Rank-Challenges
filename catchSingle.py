# rooms = list(map(int,input().split()))

# [ print(i) for i in rooms if rooms.count(i) == 1]


#The Captain's Room

# K, rooms = int(input()), input().split()

# rooms.sort()
# capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))
# print(capt_room.pop())

#Solution 2

k, rooms, single, multiple = input(), input().split(), set(), set()

for room in rooms: single.add(room) if room not in single else multiple.add(room)

print(single.difference(multiple).pop())