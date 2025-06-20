class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        k=len(nums)//2
        for key,value in count.items():
            if value>k:
                return key