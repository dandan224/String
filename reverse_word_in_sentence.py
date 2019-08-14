class Solution(object):
  def reverseWords(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    lst = list(input)
    if not lst or len(lst) == 0:
      return input
    if not ' ' in input:
      return input
    l, r = 0, len(lst) - 1
    self.reverse(lst, l, r)
    i = 0
    left = 0
    right = 0
    while i < len(lst):
      if i == len(lst) - 1 or lst[i + 1] == ' ':
        right = i
        self.reverse(lst, left, right)
        left = i + 2
      i += 1
    return ''.join(lst)

  def reverse(self, lst, left, right):
    #left, right = 0, len(lst) - 1
    while left < right:
      lst[left], lst[right] = lst[right], lst[left]
      left += 1
      right -= 1
   


