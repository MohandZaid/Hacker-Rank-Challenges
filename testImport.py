import alphabetRangoli

print(dir(alphabetRangoli))

name = 'mohand'

print(alphabetRangoli.rev(name))
print(''.join(alphabetRangoli.rev(name)))

print(alphabetRangoli.joinChar(name,'#',False))

#------------------------------------------------#


from alphabetRangoli import joinChar,rev

print(rev(name))

print(joinChar(name,'#',False))
print(joinChar(name,'#',True))
