class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num=sorted(nums)
        if num==nums:
            return True
        for i in range (len(nums)):
            nums.append(nums.pop(0))
            if num==nums:
                return True
        return False