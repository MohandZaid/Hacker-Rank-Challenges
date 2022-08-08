# Enter your code here. Read input from STDIN. Print output to STDOUT

# MY CODE 

# width = int(input())

width = 5

sym = '?' # makes option to change symbol

def upArrow(sym, width):
    symPlus = sym * 2 
    for i in range(width):
        print(sym.center(width*2-1,' '))
        sym += symPlus
        
        
def downArrow(sym, width):
    
    sym = sym*(width*2-1)
    allWidth = (width*2 - 1) + (width * 3) - (width // 2 * 2 )
    
    for i in range(width):
        print(' ' * allWidth + sym.center( width*2-1 , ' '))
        
        symList = list(sym)        
        symList.pop(0)
        
        if len(symList) == 0 : break 
        
        symList.pop(0)
        
        sym = ''
        sym = sym.join(symList)
        
def twoColumn(sym, width):        
    
    rowSym = sym*width 
    
    for i in range(width+1):
        
        print( rowSym.center((width*2-1),' ') + ' '*(width*2+1) + rowSym.center((width*2-1),' ') )
        
def middlePart(sym, width):
    
    rowSym = sym*width*2 + sym*(width*3)
    allWidth = (width*2 - 1) *2 + (width * 3) - (width // 2 * 2)
    
    for i in range(width-width//2):       
        print( rowSym.center( allWidth , ' ') )
        
def hackerRankLogo(sym, width):
    upArrow(sym, width)
    twoColumn(sym, width)
    middlePart(sym, width)
    twoColumn(sym, width)
    downArrow(sym, width)

   
hackerRankLogo(sym, width)


# REFERENCE CODE

def createTriangle(thickness):
    flag = 1
    width = thickness - 1
    totalW = width + thickness
    array = []
    for i in range(0, thickness):
        array.append(('H'*flag).center(totalW))
        flag+=2
        
    return array

def triangle(thickness):
    array = createTriangle(thickness)
    for i in range(len(array)):
        print(array[i])
    

def reversedTriangle(thickness):
    array = createTriangle(thickness)
    for i in range(len(array)):
        print((array[::-1][i]).rjust(thickness*6-1))

        
def logo(thickness):
    
    #Up side of the H
    for i in range(thickness+1):
     print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6))  
    
    #Center of the H
    for i in range(int((thickness+1)/2)):
        print(('H'*thickness*5).center(thickness*6))
     
    #Down side of the H
    for i in range(thickness+1):
     print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6)) 
   
  
def printAll(thickness):
    triangle(thickness)
    logo(thickness)
    reversedTriangle(thickness)
  
# thickness = int(input())
thickness = 5
printAll(thickness)