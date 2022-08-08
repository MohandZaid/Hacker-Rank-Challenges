if __name__ == '__main__':
    
    def check(string, any_):
        
        state = False
        if any_ == 'alphanumeric':
            
            for i in string :
                if i.isalnum():
                    state = True
                    break
            return state
        
        if any_ == 'alphabetical':
            
            for i in string :
                if i.isalpha():
                    state = True
                    break
            return state 
        
        if any_ == 'digits':
            
            for i in string :
                if i.isdigit():
                    state = True
                    break
            return state 
        
        if any_ == 'lowercase':
            
            for i in string :
                if i.islower():
                    state = True
                    break
            return state 
        
        if any_ == 'uppercase':
            
            for i in string :
                if i.isupper():
                    state = True
                    break
            return state 
    
    
    s = input()
    
    print(check(s,'alphanumeric'))
    print(check(s,'alphabetical'))
    print(check(s,'digits'))
    print(check(s,'lowercase'))
    print(check(s,'uppercase'))
    


    def check_format(string, func):
        for element in string:
            if eval(f'element.{func}()'):
                print(True)
                return

        print(False)
        return


    s = input()
    check_format(s, 'isalnum')
    check_format(s, 'isalpha')
    check_format(s, 'isdigit')
    check_format(s, 'islower')
    check_format(s, 'isupper')