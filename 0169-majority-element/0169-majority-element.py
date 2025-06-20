class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
                count+=1
            elif num==candidate:
                count+=1
            else: #if num!=candidate
                count-=1
        return candidate