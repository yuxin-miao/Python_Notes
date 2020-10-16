class Solution:
    # class of Solutions of non-specific data structure needs to use
    def reversePairs(self, nums) -> int:
        # counting inversions Offer 51
        def merge_count(l1, l2):
            count, i, j = 0, 0, 0
            list_all = []
            while i < len(l1) and j < len(l2):
                if l1[i] <= l2[j]:
                    list_all.append(l1[i])
                    i += 1
                else:
                    list_all.append(l2[j])
                    count += len(l1) - i
                    j += 1

            if i >= len(l1):
                list_all[len(list_all):] = l2[j:]
            else:
                list_all[len(list_all):] = l1[i:]
            return count, list_all

        def sort_count(input_list):
            if len(input_list) == 1:
                return 0, input_list
            else:
                left = input_list[0:int(len(input_list) / 2)]
                right = input_list[int(len(input_list) / 2):]
                count1, list1 = sort_count(left)
                count2, list2 = sort_count(right)
                count3, list3 = merge_count(list1, list2)

            count = count1 + count2 + count3
            return count, list3

        if len(nums) == 0:
            return 0
        count_all, result_list = sort_count(nums)
        return count_all

    def subsets(self, nums):
        # 78
        import copy

        def recSub(list0, subset, list1, index):
            list1.append(copy.deepcopy(subset))
            for i in range(index, len(list0)):
                subset.append(list0[i])
                recSub(list0, subset, list1, i + 1)
                subset.pop(-1)
            return

        result = []
        recSub(nums, [], result, 0)
        return result

    def commonChars(self, A):
        # 1002 find common characters
        num_str = len(A)
        index = 0
        char_dict = {}
        for str0 in A:
            for char in str0:
                if char in char_dict:
                    char_dict[char][index] += 1
                else:
                    char_dict[char] = [0] * num_str
                    char_dict[char][index] += 1
            index += 1

        char_all = []
        for key, arr in char_dict.items():
            count = set(arr)
            for i in range(0, min(count)):
                char_all.append(key)

        return char_all

    def sortedSquares(self, A):
        # 977 Square of a Sorted Array
        """ Given an array of integers A sorted in non-decreasing order,
         return an array of the squares of each number, also in sorted non-decreasing order."""
        pos = []
        neg = []
        for num in A:
            if num < 0:
                neg.insert(0, num * num)
            else:
                pos.append(num * num)

        index_pos, index_neg, index_a = 0, 0, 0
        while index_pos < len(pos) and index_neg < len(neg):
            if pos[index_pos] < neg[index_neg]:
                A[index_a] = pos[index_pos]
                index_pos += 1
            else:
                A[index_a] = neg[index_neg]
                index_neg += 1
            index_a += 1
        A[index_a:] = pos[index_pos:] + neg[index_neg:]
        return A


x = Solution()
inlist = []
for i in range(-5, 5):
    inlist.append(i - 10)
for i in range(10):
    inlist.append(i)
print(inlist)
print(x.sortedSquares(inlist))
