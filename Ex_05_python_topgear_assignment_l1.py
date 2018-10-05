
in_lst_1 = [1, 2, 2, 3]
in_lst_2 = [2, 2, 3, 3, 3, 3, 3, 3]
   
def removeSimilarEle(in_lst):
    this_ele = 'x'
    out_lst = []
    
    for ele in in_lst:
        if this_ele == ele:
            continue
        else:
            this_ele = ele
            out_lst.append(ele)
    return out_lst
    
print(removeSimilarEle(in_lst_1))
print(removeSimilarEle(in_lst_2))


