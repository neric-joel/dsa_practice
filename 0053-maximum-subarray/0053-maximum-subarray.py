class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        cur_sum=nums[0]
        for i in range (1,len(nums)):
            if cur_sum<0:
                cur_sum=0
            cur_sum=max(nums[i],cur_sum+nums[i])
            max_sum=max(max_sum,cur_sum)
        return max_sum