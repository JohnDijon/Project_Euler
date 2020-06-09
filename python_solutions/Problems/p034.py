#def dict_form():
factor_dict = {}
factor = 1
for i in range(1,10):
    for j in range(i):
        factor *=j
    factor_dict[i] = factor
print(factor_dict)
            
            