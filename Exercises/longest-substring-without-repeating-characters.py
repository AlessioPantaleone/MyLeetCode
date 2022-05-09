class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        used = {}
        start = 0
        current = 0
        if s is None:
            return 0
        for i,char in enumerate(s):
            if char not in used:
                used[char] = i
                current += 1
            else:
                longest = max(longest, current)
                current = i - max(used[char], start)
                longest = max(longest, current)
                if used[char] > start:
                    start = max (start, used[char])
                used[char] = i
            longest = max(longest, current)
        return longest


if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring("aab"))
