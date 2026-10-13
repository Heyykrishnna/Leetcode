class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans =[]
        nums.sort()

        def f(st, node):
            ans.append(node[:])

            for i in range(st, len(nums)):
                if i > st and nums[i] == nums[i-1]:
                    continue
                node.append(nums[i])
                f(i+1, node)
                node.pop()

        f(0, [])
        return ans