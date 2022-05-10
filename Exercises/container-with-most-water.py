class Solution:
    def maxArea(self, heights: [int]) -> int:
        m = 0
        lpointer = 0
        rpointer = len(heights) - 1
        while rpointer > lpointer:
            m = max(m,min(heights[lpointer],heights[rpointer])*(rpointer-lpointer))
            if heights[lpointer] > heights[rpointer]:
                rpointer -= 1
            else:
                lpointer += 1
        return m

    def maxAreaBruteForce(self, heights: [int]) -> int:
        m = 0
        for i, height in enumerate(heights):
            for j in range (len(heights) - i):
                m = max(min(height,heights[j+i])*j,m)
        return m


if __name__ == "__main__":
    S = Solution()

    print(S.maxArea([1,8,6,2,5,4,8,3,7]))