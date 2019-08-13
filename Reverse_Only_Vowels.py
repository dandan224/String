class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if not input:
        return input
    lst = list(input)
    vowel_lst = ['a','e','i','o','u']
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] not in vowel_lst:
           left += 1
        elif lst[right] not in vowel_lst:
           right -= 1
        else:
            lst[left],lst[right] = lst[right],lst[left]
            left += 1
            right -= 1
    return ''.join(lst)
