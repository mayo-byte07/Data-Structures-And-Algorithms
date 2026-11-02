import collections

class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = collections.Counter(arr)
        freq_values = counts.values()
        return len(freq_values) == len(set(freq_values))