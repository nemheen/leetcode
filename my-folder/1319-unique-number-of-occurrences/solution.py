import numpy as np
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = np.array(arr)
        c = collections.Counter(arr)

        return len(c) == len(set(c.values()))


        
