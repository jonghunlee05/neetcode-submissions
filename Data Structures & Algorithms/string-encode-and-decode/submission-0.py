class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_word = ""

        for word in strs:

            encoded_word += str(len(word)) + "#" + word

        return encoded_word


    def decode(self, s: str) -> List[str]:


        answer = []

        
        i = 0


        while i < len(s):

            j = s.find("#", i)

            lenner = int(s[i:j])

            answer.append(s[j + 1: j + 1 + lenner])


            i = j + 1 + lenner



        return answer


