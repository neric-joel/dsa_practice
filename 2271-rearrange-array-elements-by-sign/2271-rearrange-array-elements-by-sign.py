class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans

