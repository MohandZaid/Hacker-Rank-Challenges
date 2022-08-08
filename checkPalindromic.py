# numbers = list(map( int , input().split()))

# checknum = []

# def checkPositive(num):
#     if num < 0 :
#         checknum.append(False)
#     else :
#         checknum.append(num)
    
# def checkPalindromic(checknum):
#     checknum = list(map(str, checknum))
#     checknum = list(map(list,checknum))
    
#     for num in checknum:
#         n = num.copy()
#         num.reverse()
#         if num == n :
#             return True
#     return False            

# for num in numbers:
#     checkPositive(num)

# if all(checknum):
#     print(checkPalindromic(checknum))

# else :
#     print(False)


# integers = input().split()
# print(
#         all(map(lambda x: int(x)>0, integers)) and 
#         any(map(lambda x: x==x[::-1], integers))
#      )


ls = ['21', '31', '-3']
for i in ls:
    print(i[::-1])
