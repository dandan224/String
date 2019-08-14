# solution #1:(hash map)
class Solution(object):
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    freq = {}
    input_lst = []
    for i in input:
        if i.isalnum():
            input_lst.append(i)
    for i in range(len(input_lst)):
        if input_lst[i] in freq:
            freq[input_lst[i]] = freq[input_lst[i]] + 1
        else:
            freq[input_lst[i]] = 1
    odd_cnt = 0
    for key in freq.keys():
        if freq[key] % 2 == 1:
            odd_cnt += 1
            if odd_cnt > 1:
                return False
    return True
    
   # solution #2:(reverse)
  class Solution(object):
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    lst = []
    input = input.lower()
    for i in input:
        if i.isalnum():
            lst.append(i)
    
    if not lst or len(lst) <= 1:
      return True
    lst_new = self.reverse(lst)
    if lst_new == lst:
      return True
    return False
    

  def reverse(self, input):
      l = list(input)
      left, right = 0, len(input) -1
      while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
      return l
    
   
