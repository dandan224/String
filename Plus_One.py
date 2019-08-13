class Solution(object):
  def plus(self, digits):
    """
    input: int[] digits
    return: int[]
    """
    # write your solution here
    if not digits:
      return
    if len(digits) == 0:
      digits[0] = 1
      return digits
    carry = 0
    if digits[len(digits) - 1] + 1 >= 10:
      digits[len(digits) - 1] = (digits[len(digits) - 1] + 1) % 10
      carry = 1
    else:
      digits[len(digits) - 1] = digits[len(digits) - 1] + 1
      carry = 0
    for i in range(len(digits) - 2, -1, -1):  
      res = digits[i] + carry
      if res >= 10:
        digits[i] = res% 10
        carry = 1
      else:
        digits[i] = res
        carry = 0
    if carry == 1:
      digits.insert(0,1)
    return digits
    
    # time: O(n)
