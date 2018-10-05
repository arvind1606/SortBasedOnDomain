
in_lst_1 = ['axa', 'xyz', 'gg', 'x', 'yyy'];
in_lst_2 = ['x', 'cd', 'cnc', 'kk']
in_lst_3 = ['bab', 'ce', 'cba', 'syanora']
   
def strChk(in_lst):
    count = 0
    for ele in in_lst:
        # check if element len is more than 2
        # and first and last chars of the string are the same
        if len(ele) > 2 and ele[0] == ele[-1]:
            #print(ele)
            count+=1            
    return count

print(strChk(in_lst_1))
print(strChk(in_lst_2))
print(strChk(in_lst_3))
