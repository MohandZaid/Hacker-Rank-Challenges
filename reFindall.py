import re

# string = input()
# string = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
string = 'abaabaabaabaaefEAEOUOIouf'
# string = 'abaabaabaabaaei'
# string = 'abaabaabaabaae'


# pattern = r'(?:[^AEIOUaeiou])([AEIOUaeiou]{2,})(?:[^AEIOUaeiou])'
# pattern = r'[^AEIOUaeiou]?([AEIOUaeiou]{2,})[^AEIOUaeiou]+'
pattern = r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])'

matched = re.findall(pattern, string, re.I)
# matched = re.findall(pattern, string)
# matched = re.finditer(pattern, string)

if not matched : print(-1)

[ print(m) for m in matched if len(m) >= 2 ]

# print(list(map(lambda x : x.group() , matched)))