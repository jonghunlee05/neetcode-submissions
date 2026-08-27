class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) - 1
        isPalindrome = True


        while left_idx < right_idx:
            while left_idx < right_idx and not s[left_idx].isalnum():
                left_idx += 1

            while left_idx < right_idx and not s[right_idx].isalnum():
                right_idx -= 1

            if s[left_idx].lower() != s[right_idx].lower():
                isPalindrome = False
                break

            left_idx += 1
            right_idx -= 1

        return isPalindrome