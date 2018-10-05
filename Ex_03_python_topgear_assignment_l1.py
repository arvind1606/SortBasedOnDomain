
in_lst_1 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
in_lst_2 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
   
def strChk(in_lst):
    lst_x = []
    lst_nonX = []
    out_lst = []
    
    for ele in in_lst:
        # check if element starts with x or X
        if ele[0] == 'x' or ele[0] == 'X':
            lst_x.append(ele)
        else:
            lst_nonX.append(ele)

    # mearge two lists after sorting    
    out_lst = sorted(lst_x) + sorted(lst_nonX)
    return out_lst              

print(strChk(in_lst_1))
print(strChk(in_lst_2))

