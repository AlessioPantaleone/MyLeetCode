class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        maxwealth = 0
        for customer in accounts:
            whealth =  sum(customer)
            maxwealth = max(maxwealth,whealth)
        return maxwealth


if __name__ == "__main__":
    acc = [[6,67],[4,4,4],[1,2,3]]
    S = Solution()
    print(S.maximumWealth(acc))