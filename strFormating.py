def print_formatted(number):
    
    n = len(bin(number)[2:]) 
    
    for i in range(number):
        
        print( str(i+1).rjust(n) ,
        oct(i+1)[2:].rjust(n) ,
        hex(i+1)[2:].upper().rjust(n) ,
        bin(i+1)[2:].rjust(n) )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)