'''def pattern1(n):
    for row in range(n):
        # for colums in each row
        for col in range(n-row):
            print('#',end=' ')
        print('')
# by default end = '\n'
pattern1(5) '''



def pattern(n):
    for i in range(n):
        for j in range(i):
            print(j+1,end=' ')
        print( )
    for i in range(n):
        for j in range(n-i):
            print(j+1,end=' ')
        print()        
pattern(5)         

'''
def pattern(n):
    for i in range(n):
        for j in range(n):
            if j in range(i):
                print(' ',end=' ')
            else:
             print(j,end=' ')
        print( )
pattern(5)       '''   


'''
def pattern(n):
    for i in range(n):
        for j in range(n):
            if j in range(n-i):
                print(' ',end=' ')
            else:
             print('*',end=' ')
        print( )
pattern(5)            '''

#left cross pyramid
'''
def cspyramid(n):
    for i in range(n):
        for j in range(n):
            if j in range(i):
                print(' ',end=' ')
            else:
             print('*',end=' ')    
        print()

def pattern(n):      
       for i in range(n):
         for j in range(n):
            if j in range(n-i):
                print(' ',end=' ')
            else:
             print('*',end=' ')    
         print()   
pattern(4)

cspyramid(4)    '''

#pyramid
'''
def patternv(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ') 
        for k in range(2*i+1):
            print('*',end=' ') 
        print()  
patternv(5)        ''' 

#rows = 3  # You can change this to increase the number of rows
'''
for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()  # Newline after each row'''


#inverted pyramid
'''
 def invpyramid(n):
    for i in range(n-1,-1,-1):
        for j in range(n-i-1):
            print(' ',end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print() 
invpyramid(5)           '''

#diamond pyramid
'''
def diamond(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()
     
    for i in range(n-2,-1,-1):
        for j in range(n-i-1):
            print(' ',end=' ')
        for k in range(2*i+1):
            print('*',end=' ') 
        print()       
diamond(3)             '''

