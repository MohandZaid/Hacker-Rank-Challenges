length, width = list(map(int,input().split()))
fill_char = '-'
pattern = '.|.'

def upper_part(pattern):
    for _ in range(length // 2):
        print(pattern.center(width, fill_char))
        pattern += '.|..|.'

def lower_part(pattern):
    pattern *= (length - 2)
    for _ in range(length // 2):
        print(pattern.center(width, fill_char))
        pattern = pattern[6:]

def welcome():
    print('welcome'.upper().center(width, fill_char))

def door_mat():
    upper_part(pattern)
    welcome()
    lower_part(pattern)
    
door_mat()