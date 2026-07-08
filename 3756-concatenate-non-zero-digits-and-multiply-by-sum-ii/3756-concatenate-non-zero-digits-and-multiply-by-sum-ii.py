class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        sums = [0] * (n + 1)
        nums = [0] * (n + 1)
        count = [0] * (n + 1)
        power = [1] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)

            sums[i + 1] = sums[i] + digit
            nums[i + 1] = nums[i]
            count[i + 1] = count[i]

            if digit:
                nums[i + 1] = (nums[i] * 10 + digit) % MOD
                count[i + 1] += 1

            power[i + 1] = power[i] * 10 % MOD

        ans = []

        for left, right in queries:
            right += 1

            length = count[right] - count[left]
            number = (nums[right] - nums[left] * power[length]) % MOD
            ds = sums[right] - sums[left]

            ans.append(number * ds % MOD)

        return ans