import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []
        
        for spell in spells:
            min_potion = (success + spell - 1) // spell
            idx = bisect.bisect_left(potions, min_potion)
            ans.append(m - idx)
            
        return ans