class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        # taks the minimum between the two ehgiht -> multiply by it's distance. shift whichever is the one that's les.. 
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r and l < len(heights):
            
            current_area = min(heights[l], heights[r]) * (r - l)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            max_area = max(max_area, current_area)

        return max_area