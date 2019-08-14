class Solution(object):
  def validPalindrome(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    lst = list(input)
    left, right = 0, len(lst) -1
    if self.isPalindrome(lst):
      return True
    while left <= right:
      if lst[left] == lst[right]:
        left += 1
        right -= 1
        # return True
      else:
        if self.isPalindrome(lst[:left ] + lst[left+1:]):
          return True
        if self.isPalindrome(lst[:right] + lst[right + 1:]):
          return True
        break
    return False

  def isPalindrome(self, input):
    lst= input
    lst1 = lst[::-1]
    if lst == lst1:
      return True
    return False
