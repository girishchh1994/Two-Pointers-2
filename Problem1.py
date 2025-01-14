Time Complexity: O(n)
Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return nums
        k = 2
        count = 1
        j = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <=k:
                nums[j] = nums[i]
                j += 1
        return j
