class Solution:
    def trap(self, heights: [int]) -> int:
        trapped = 0
        partialtrapped = 0
        current = heights[0]

        for height in heights[1:]:
            if height <= current:
                partialtrapped += current-height
            else:
                current = height
                trapped +=partialtrapped
                partialtrapped = 0
        trapped+=partialtrapped

        highest = max(heights)
        highestfornow = 0

        for height in reversed(heights):
            if height == highest: break
            highestfornow = max (highestfornow,height)
            trapped -= highest - max(height,highestfornow)

        return trapped


if __name__ == "__main__":
    S = Solution()

    print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))