class Solution:
    def isValid(self, s: str) -> bool:
        answer = []
        isValid = True
        syn = { "{" : "}", "[" : "]", "(" : ")" }


        for i in range(len(s)):

            if s[i] in syn:
                answer.append(s[i])
            else:
                if len(answer) == 0 or syn[answer[-1]] != s[i]:
                    isValid = False
                else:
                    answer.pop()
        

        if len(answer) != 0:
            isValid = False

        return isValid