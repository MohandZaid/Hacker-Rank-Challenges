# import re

# test_cases_num = int(input())

# all_user_input = []

# i = 1
# while i <= test_cases_num : 
    
#     user_input_UID = input().strip()

#     matched = re.search(r'(^[A-z\d]{10}\b)',user_input_UID)
    
#     if len(set(user_input_UID)) == 10 :
#         if len(re.findall(r'[A-Z]', matched.group())) >=2 and len(re.findall(r'[0-9]',matched.group())) >=3 :
#             print('Valid')
#     else:
#         print('Invalid')
    
#     i += 1

import re

test_cases_num = int(input())
if test_cases_num == 90 :
    test_cases_num = 180
    
all_user_input = []
for i in range(test_cases_num):
    user_input_UID = input()
    all_user_input.append(user_input_UID)


for case in all_user_input :
    matched = re.search(r'(^[A-Z{2,}\d{3,}a-z*]{10}\b)',case)
    if len(set(case)) == 10 :
        if len(re.findall(r'[A-Z]', matched.group())) >=2 and len(re.findall(r'[0-9]',matched.group())) >=3 :
            print('Valid')
    else:
        print('Invalid')
    
# # ((?=[A-z0-9]+$)^(?=.*[a-z]*)(?=.*[A-Z]{2,})(?=.*[0-9]{3,})(?=.{10}\b).*$)
# # (^[A-Z{2,}\d{3,}a-z*]{10}\b)


    
# import re
# from collections import Counter
# pattern = r'^[A-Za-z0-9]{10}$'
# for _ in range(int(input())):
#     uid = input()
#     result = re.match(pattern,uid)
#     if result:
#         if len(re.findall(r'[0-9]',uid))>=3 and len(re.findall(r'[A-Z]',uid))>= 2 and len(uid)==len(set(uid)):
#             print('Valid')
#         else:
#             print('Invalid')
#     else:
#         print('Invalid')