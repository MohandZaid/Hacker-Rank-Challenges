# from operator import itemgetter 

def person_lister(f):
    def inner(people):

        people.sort(key= lambda x : int(x[2]))

        # return [f(n) for n in people]
        return people
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print('------------')
    print(*name_format(people), sep='\n')

'''
#INPUT

10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M

#OUTPUT
Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael
'''

# Solution 2

# def person_lister(f):
#     def inner(people):
#         # complete the function
#         return map(f, sorted(people, key=lambda x: x[2]))          
#     return inner

# Solution 3

# from operator import itemgetter 

# def person_lister(f):
#     def inner(people):
#         for prs in people:
#             prs[2] = int(prs[2])
            
#         people.sort(key=itemgetter(2))

#         return [f(n) for n in people]
#     return inner