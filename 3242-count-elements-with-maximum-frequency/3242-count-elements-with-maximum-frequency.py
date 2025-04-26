from collections import defaultdict
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        maxfreq=max(freq.values() if freq else 0)
        k=sum(count for count in freq.values() if count == maxfreq)
        return k