
in_lst = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', \
          'www.website.org', 'www.bis.org.in', 'www.rbi.org.in'];
   
in_lst_dict = {}

# Splitting the urls based on "."
for element in in_lst:
    ele = element.split(sep='.')
    # adding the splitted values to dictonary
    # where key is domain and value is url
    in_lst_dict.update({str(ele[-1]) : str(element)})

# sort the dict based on domain
in_lst_dict = sorted(in_lst_dict.items())

out_lst = []
for key in in_lst_dict:
    # append all the values in sorted order of keys
    out_lst.append(key[1])
    
print(out_lst)
    
