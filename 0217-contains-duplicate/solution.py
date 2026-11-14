from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        for key, value in counts.items():
            if value > 1:
                return True
                break
        return False
