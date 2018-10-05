
in_lst_1 = [(1, 3), (3, 2), (2, 1)]
in_lst_2 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
   
def tupleSort(in_lst):
    ele_count = len(in_lst)
    
    for key_tpl_idx in range(0, ele_count):
        for curr_tpl_idx in range(key_tpl_idx+1, ele_count):
            # take list elements one by one and sort
            if in_lst[key_tpl_idx][-1] > in_lst[curr_tpl_idx][-1]:
                tmp = in_lst[key_tpl_idx]
                in_lst[key_tpl_idx] = in_lst[curr_tpl_idx]
                in_lst[curr_tpl_idx] = tmp
    #print(in_lst)
    
tupleSort(in_lst_1)
print(in_lst_1)
tupleSort(in_lst_2)
print(in_lst_2)

