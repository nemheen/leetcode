import itertools

class Solution:

    

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    
        def longest_prefix(a, b):
            pref = []

            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    pref.append(a[i])
                else:
                    break
            return len(pref)
            
        longest = 0
        arr1 = sorted(map(str, arr1))
        arr2 = sorted(map(str, arr2))

        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            a, b = arr1[i], arr2[j]
            pref = longest_prefix(a, b)
            longest = max(longest, pref)

            if a < b:
                i += 1
            else:
                j += 1

        return longest
        

