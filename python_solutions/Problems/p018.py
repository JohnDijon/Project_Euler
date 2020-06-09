#use triangel in a form:
#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#....

def open_trangle():
    """ opens and transform the digit grit to a matrix_list """
    with open('other_files/p018_triangle.txt') as num_file:
        tree_list = []
        current_tree_list = []
        current_str =''
        num_str=''
       
        for line in num_file:
            num_str += line.rstrip() + ' '
            
            for digit in num_str:
                if digit == ' ':
                    current_tree_list.append(int(current_str))
                    current_str =''
                else:
                    current_str += digit
            tree_list.append(current_tree_list)
            num_str = ''
            current_tree_list = []
    return tree_list

def node_adder(array, row, pos):
    """ find best sum for donw adjacent numbers, goes from bottom to the top """
    sum1 = array[row][pos] + array[row+1][pos]
    sum2 = array[row][pos] + array[row+1][pos+1]
    if sum1 > sum2:
        best_sum = sum1
    else:
        best_sum = sum2 
    return best_sum

def problem_solve(): 
    """
    optimal way is to sum nodes form bottom to the top, assigning the best sum 
    to the corresponding node. This ways the triangle will be sorted, and the top
    element will be the largest sum 
    
    """
    tree_list = open_trangle()
    for row in range(len(tree_list)-2, -1, -1):
#        print(len(tree_list), row)
        for pos in range(len(tree_list[row])):
#            print(row, pos, ":   ", node_adder(tree_list, row, pos))
            tree_list[row][pos] = node_adder(tree_list, row, pos)
    return tree_list[0][0]
    
if __name__ == "__main__":
    print(problem_solve())