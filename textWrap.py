import textwrap

def wrap(string, max_width):
    
    string = string.strip()
    
    strBuffer = ''  
    outString = ''
    
    tempString = string.split(' ')
    string = ''
    for i in tempString:
        string += i
        
    del tempString
    
    string = list(string)
    
    for i in range(len(string)):
                
        strBuffer += string[i]
        
        if len(strBuffer) == max_width :
            outString += strBuffer + '\n'
            strBuffer = ''
        
        elif i == string.index(string[-1]) :
            outString += strBuffer
        
    return outString
    
    
if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string = 'bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd'
    max_width = 20
    result = wrap(string, max_width)
    print(result)