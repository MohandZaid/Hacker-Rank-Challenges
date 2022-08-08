import re

def check_float(input_num):
    pattern = r"(^[\+|\-]?\d*?\.\d+$)"
    matched = re.search(pattern, input_num)
    if matched :
        return True
    return False

num_of_lines = int(input())

for _ in range(num_of_lines):
    user_num = input()
    if check_float(user_num):
        print("True")
        continue
    print("False")


"""
#INPUT

5
1.414
+.5486468
0.5.0
1+1.0
0
"""