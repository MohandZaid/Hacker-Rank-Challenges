import re

def check_regex(input_pattern):
    try:
        pattern = fr"{input_pattern}"
        matched = re.search(pattern, 'some123S')
        return True
    except:
        return False

num_of_lines = int(input())

for _ in range(num_of_lines):
    user_num = input()
    if check_regex(user_num):
        print("True")
        continue
    print("False")

'''
# INPUT

2
.*\+
.*+
'''
# see compile() function