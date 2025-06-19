from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        for x,v in count.items():
            if v==1:
                return x