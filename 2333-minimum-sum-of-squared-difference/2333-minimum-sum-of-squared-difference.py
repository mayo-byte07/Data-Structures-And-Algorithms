class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        if k >= sum(diff):
            return 0
        buckets = [0] * 100001
        max_d = 0
        for d in diff:
            buckets[d] += 1
            if d > max_d:
                max_d = d
        for i in range(max_d, 0, -1):
            if buckets[i] > 0:
                if k >= buckets[i]:
                    k -= buckets[i]
                    buckets[i - 1] += buckets[i]
                    buckets[i] = 0
                else:
                    buckets[i - 1] += k
                    buckets[i] -= k
                    k = 0
                    break
        ans = 0
        for i in range(max_d, 0, -1):
            if buckets[i] > 0:
                ans += buckets[i] * i * i
        return ans