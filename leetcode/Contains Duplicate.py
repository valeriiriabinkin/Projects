class Solution(object):
    def containsDuplicate(self, nums):
        if nums == [i for i in range(len(nums))]:
            return False
        for i in range(len(nums)):
            num = nums[0]
            nums.pop(0)
            if num in nums:
                return True
        else:
            return False