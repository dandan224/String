##Solution #1(inplace)
class Solution(object):
  def remove(self, input, t):
    """
    input: string input, string t
    return: string
    """
    # write your solution here
    lst = list(input)
    lst_t = list(t)
    i,j = 0,0
    while j < len(lst):
        if lst[j] not in lst_t:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])
 
 # solution #2:
 new_lst = []
    for i in range(len(lst)):
      if lst[i] not in lst_t:
        new_lst.append(lst[i])
    return ''.join(new_lst)

   
