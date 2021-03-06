class Solution:
    def canPartition(self, nums) -> bool:
        # 416 Equal partition
        # dynamic programming solution
        sum_list = sum(nums)
        target = sum_list // 2
        if target * 2 != sum_list:
            return False

        subset = [[False for i in range(target + 1)] for i in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            subset[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j < nums[i - 1]:
                    subset[i][j] = subset[i - 1][j]
                else:
                    subset[i][j] = subset[i - 1][j] or subset[i - 1][j - nums[i - 1]]

        def find_num(curr_target, index, result):  # used for print the subset 
            if index == 0 and curr_target != 0 and subset[1][curr_target]:
                result.append(nums[index])
                print(result)
                return True
            if curr_target == 0:
                print(result)
                return True
            if subset[index][curr_target]:
                new_result = result.copy()
                find_num(curr_target, index - 1, new_result)
            if curr_target >= nums[index]:
                if subset[index][curr_target - nums[index]]:
                    find_num(curr_target - nums[index], index - 1, result)

        return subset[len(nums)][target]
        # find_num(target, len(nums) - 1, [])

    def canPartition2(self, nums) -> bool:
        # 416 recursive solution, however time exceed on LeetCode 

        def isSum(index, target):
            if target == 0:
                return True
            if index == 0 and target != 0:
                return False
            if nums[index - 1] > target:
                return isSum(index - 1, target)
            return isSum(index - 1, target - nums[index - 1]) or isSum(index - 1, target)
        sum_list = sum(nums)
        target = sum_list // 2
        if target * 2 != sum_list:
            return False
        return isSum(len(nums), target)


x = Solution()
print(x.canPartition2([1, 15, 7, 7]))
