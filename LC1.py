def twoSum(self, nums, target):
# 1.twosum
    for i in range(0, len(nums)):
        for j  in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]


print(twoSum(1, [2,7,11,15], 9))
