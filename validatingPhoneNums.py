import re

num_of_inputs = int(input())

pattern = r'(^[7-9][\d]{9}\b)'

for _ in range(num_of_inputs):
    phone_num = input().strip()
    
    matched = re.search(pattern,phone_num)
    
    if matched is None :
        print('NO')
        continue
        
    print('YES')
       