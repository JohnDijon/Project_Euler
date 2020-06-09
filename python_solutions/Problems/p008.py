#load the 1000 digit list from txt file. It's saved in str
with open('other_files\8.txt') as num_file:
    num_str=''
    for line in num_file:
        num_str += line.rstrip()

#digit str saved in list
num_list=[]
for num in num_str:
    num_list.append(int(num))

def list_multiply(current_list):
    """
    Fucntion that multiplys 13 digits from a list(takes a list). 
    Reterns tuple of product and list itself
    """
    current_str = ''
    current_try = 1
    for j in range(13):
        current_try = current_try * current_list[j]
        
    for i in range(13):
        current_str += str(current_list[i])
    
    return (current_try, current_str)

#loop through the 1000digit list, multiplying and comparing the products 
best_try=1
best_str = ''
for i in range(len(num_list)-13):
    current_tuple = list_multiply(num_list[i:i+13])
    if current_tuple[0] > best_try:
        best_try = current_tuple[0]
        best_str = ''
        best_str = current_tuple[1]
print('Product:', best_try, '\nSequence:', best_str, '\nLength:', len(best_str))