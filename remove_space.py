# Solution #1, inplace 
# consider all the cases, in the while loop, just keep the j moving ahead.
class Solution(object):
  def removeSpaces(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if not input or len(input) == 0:
      return input
    lst = list(input)
    i = j = 0
    while j < len(lst):
      # j not space or j is space and i is not the first element
      # the element before i is not space, continue
      if lst[j] != ' ' or (i != 0 and lst[i - 1] != ' '):
        lst[i] = lst[j]
        i += 1
      j += 1
      # remove trailing empty space
    if i > 0 and lst[i - 1] == ' ':
      i -= 1
    return ''.join(lst[:i])
    
# solution #2, create a new list
def remove_spaces(input):
    if not input or len(input) == 0:
        return input
    lst = []
    lst1 = list(input)
    for fast in range(len(lst1)):
        if input[fast] == ' ' and (fast == 0 or lst1[fast - 1]== ' '):
            continue
        lst.append(lst1[fast])
    if len(lst) > 0 and lst[-1] == ' ':
        lst.pop()
    return ''. join(lst)
