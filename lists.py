if __name__ == '__main__':
    N = int(input())
    
    outList = []
    
    while N != 0:
        
        command = input()
        
        command = command.split(' ')
        
        if len(command) == 3 :
            
            command[1] = int(command[1])
            command[2] = int(command[2])
            
            if command[0] == 'insert' :
                outList.insert( command[1], command[2] )
        
        elif len(command) == 2 :
            
            command[1] = int(command[1])
            
            if command[0] == 'remove' :
                outList.remove(command[1])
            
            elif command[0] == 'append' :
                outList.append(command[1])
                
        elif len(command) == 1 :
            
            if command[0] == 'print' :
                print(outList)
            
            elif command[0] == 'sort' :
                outList.sort()
            
            elif command[0] == 'pop' :
                outList.pop()
                
            elif command[0] == 'reverse' :
                outList.reverse()
        N-=1