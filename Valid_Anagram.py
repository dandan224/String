# Solution #1 (by using sort)
class Solution(object):
  def isAnagram(self, source, target):
    """
    input: string source, string target
    return: boolean
    """
    # write your solution here
    lst1 = list(source)
    lst2 = list(target)
    return sorted(lst1) == sorted(lst2)
    
    
    # solution #2 (compare the length of the two string and count the number of the letter)
    class Solution(object):
  def isAnagram(self, source, target):
    """
    input: string source, string target
    return: boolean
    """
    # write your solution here
    lst1 = list(source)
    lst2 = list(target)
    if len(lst1) != len(lst2):
      return False
    freq_1 = {}
    freq_2 = {}
    for i in range(len(lst1)):
        if lst1[i] in freq_1:
            freq_1[lst1[i]] = freq_1[lst1[i]] + 1
        else:
            freq_1[lst1[i]] = 1
    for j in range(len(lst2)):
      if lst2[j] in freq_2:
        freq_2[lst2[j]] = freq_2[lst2[j]] + 1
      else:
        freq_2[lst2[j]] = 1
    return freq_1 == freq_2
