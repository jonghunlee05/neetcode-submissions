class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = 0
        answer = nums[0]
        R = len(nums) - 1

        while L <= R: 
            if nums[L] < nums[R]:
                answer = min(answer, nums[L])
                break

            mid = (R + L) // 2
            answer = min(answer, nums[mid])

            if nums[L] <= nums[mid]:
                L = mid + 1
            else:
                R = mid - 1

        return answer


