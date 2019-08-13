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
   
