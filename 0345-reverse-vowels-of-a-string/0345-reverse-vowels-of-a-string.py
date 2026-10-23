class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        chars = list(s)
        left = 0
        right = len(chars) - 1
        
        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return "".join(chars)