class Solution:
    def canPartition(self, nums) -> bool:
        # 416 Equal partition
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


x = Solution()
print(x.canPartition([100, 100, 100, 100]))
