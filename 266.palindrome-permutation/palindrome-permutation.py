class Solution(object):
  def canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    evenCount = 0
    oddCount = 0
    d = {}
    # Put each charcters into a Dictionary such as {'a':2,'b':1}
    for c in s:
        d[c] = d.get(c,0)+1
    # Count odd charcters and even charcters.
    for k in d:
        if d[k] % 2 == 1:
            oddCount += 1
        else:
            evenCount += 1
    # Only if oddCount == 1 or oddCount == 0 return True
    if len(s) % 2 == 1:
        if oddCount == 1:
            return True
    else:
        if oddCount == 0:
            return True
    return False
