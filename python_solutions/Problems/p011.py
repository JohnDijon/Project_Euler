def open_file():
    """ opens and transform the digit grit to a matrix_list """
    with open('other_files/11.txt') as num_file:
        digit_list = []
        current_digit_list = []
        current_str =''
        num_str=''
       
        for line in num_file:
            num_str += line.rstrip() + ' '
            
            for digit in num_str:
                if digit == ' ':
                    current_digit_list.append(int(current_str))
                    current_str =''
                else:
                    current_str += digit
            digit_list.append(current_digit_list)
            num_str = ''
            current_digit_list = []
#    return  digit_list
print(digit_list)
def element_check(element, digit_list):
    """
    checks all producta for elenemt A[m][n] (taken as (m, n)).
    It conciders that horizontal product for element A[m][n] to the right 
    equals to A[m][n+3] to the left, as well vertical A[m][n] down equals to
     A[m+3][n] up. The same concideration was taken for diagonals, so only 
    down diagonals (both to the left and to the right) were found.
    Whenever borders of the matrix were excided, product = 0 was returned      
    """
    m = element[0]
    n = element[1]
    try:
        horizontal = (digit_list[m][n]*digit_list[m][n+1]*
                      digit_list[m][n+2]*digit_list[m][n+3])
    except IndexError:
        horizontal = 0   #to avoid none
    try:
        vertical = (digit_list[m][n]*digit_list[m+1][n]*
                    digit_list[m+2][n]*digit_list[m+3][n])
    except IndexError:
        vertical = 0
    try: 
        right_diagonal = (digit_list[m][n]*digit_list[m+1][n+1]*
                    digit_list[m+2][n+2]*digit_list[m+3][n+3])
    except IndexError:
        right_diagonal = 0
    try:
        left_diagonal = (digit_list[m][n]*digit_list[m+1][n-1]*
                    digit_list[m+2][n-2]*digit_list[m+3][n-3])
    except IndexError:
        left_diagonal = 0
    
    best_multiple = sorted((horizontal, vertical, right_diagonal, 
                            left_diagonal), reverse = True)[0]

    return best_multiple


def problem_solve():
    current_best = 0
    digit_list = open_file()
    for row in range(len(digit_list)):
        for col in range(len(digit_list[row])):
            current = element_check((row, col), digit_list)
            #print(current) 
            if current_best < current:
                current_best = current

    return current_best

if __name__ == "__main__":
    print(problem_solve())