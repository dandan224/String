class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    lst = list(input)
    
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return ''.join(lst)
