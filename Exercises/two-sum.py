class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        Ducc = {}
        for i, num in enumerate(nums):
            if target-num in Ducc:
                return [i, Ducc[target-num]]
            Ducc[num] = i

if __name__ == "__main__":
    S = Solution()
    print(S.twoSum([2,7,11,15],18))