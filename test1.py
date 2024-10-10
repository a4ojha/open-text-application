# Test #1: Print a triangle

# Prints a right triangle with M width and N height in one line of code
def display_triangle(M, N):
    '''
    M, N: int > 0
    rtype: None, prints to console
    '''
    [print('*  ' * (M * i // N if M * i % N == 0 else M * i // N + 1)) for i in range(1, N + 1)]    


# Test: prints a triangle with width 3 and height 4
display_triangle(3, 4)

'''
Examples:

M = 3, N = 4:
3 is the width, 4 is the height
*  
*  *  
*  *  *  
*  *  *  

M = 5, N = 5
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
'''