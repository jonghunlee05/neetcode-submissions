class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        nums.sort()

        for i in range(len(nums)):

            if nums[i] > 0: 
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left_idx = i + 1
            right_idx = len(nums) - 1

            while left_idx < right_idx:
                totalSum = nums[i] + nums[left_idx] + nums[right_idx]

                if totalSum < 0: 
                    left_idx += 1
                elif totalSum > 0: 
                    right_idx -= 1
                else:
                    answer.append([nums[i], nums[left_idx], nums[right_idx]])
                    
                    left_idx += 1
                    right_idx -= 1
                    while nums[left_idx] == nums[left_idx - 1] and left_idx < right_idx:
                        left_idx += 1




        return answer