class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            next_groups = []
            for i in range(0, len(s), k):
                group_sum = sum(int(ch) for ch in s[i:i + k])
                next_groups.append(str(group_sum))
                
            s = "".join(next_groups)
            
        return s