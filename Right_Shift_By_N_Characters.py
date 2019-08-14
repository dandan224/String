class Solution(object):
  def rightShift(self, input, n):
    """
    input: string input, int n
    return: string
    """
    # write your solution here
    if not input or len(input) <= 1:
      return input
    n = n%len(input)
    return input[-n:] + input[:-n] 
