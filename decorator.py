def deco(func):
    def nested():
        print('decoOne')
        func()
    return nested

def deco2(func):
    def nested(name='mozaid'):
        print(name.upper())
    return nested

@deco
def sayName(name='mohand zaid'):
    return name

@deco2
def sayName2(name):
    print(name)

name = 'mohand abdelaleem zaid'


sayName()
sayName2(name)
