class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        gcd_length = get_gcd(len(str1), len(str2))
        return str1[:gcd_length]