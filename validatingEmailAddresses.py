import re

def check_valid_email(email_from_user):
    pattern = r'(^<[a-z]+[\wl\.-]+?@[a-z]+\.[a-z]{1,3}>)'
    matched = re.search(pattern,email_from_user)
    if matched :
        return True
    return False


num_of_lines = int(input())
valid_email = []

for _ in range(num_of_lines):
    name_email = input().split()
    if check_valid_email(name_email[1]):
        # print(' '.join(name_email))
        valid_email.append(' '.join(name_email))

print('#'*25)

for valid in valid_email:
    print(valid)


'''
# INPUT
22
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>
'''