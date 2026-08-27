class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        groups = {}
        

        for i in nums:

            key = i

            if i not in groups:
                groups[key] = 0

            groups[key] += 1
        

        temp = sorted(groups.items(), key=lambda item : item[1], reverse=True)

        answer = []

        for key, value in temp[:k]:
            answer.append(key)


        return answer




