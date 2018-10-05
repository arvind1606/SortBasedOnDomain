# SortBasedOnDomain

1.	Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; Sort the list based on the top level domain (edu, com, org, in) using custom sorting

2.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  

i.	['axa', 'xyz', 'gg', 'x', 'yyy']
ii.	['x', 'cd', 'cnc', 'kk']
iii.	['bab', 'ce', 'cba', 'syanora']

3.	Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
Hint: this can be done by making 2 lists and sorting each of them before combining them.
i.	['bbb', 'ccc', 'axx', 'xzz', 'xaa']
ii.	['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
      Hint: use a custom key= function to extract the last element form each tuple.
i.	 [(1, 3), (3, 2), (2, 1)]
ii.	[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

5.	Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
i.	 [1, 2, 2, 3], [2, 2, 3, 3, 3]

