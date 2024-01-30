import numpy as np
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []
        result.append(list(set(nums1[i] for i in range(len(nums1)) if not any(nums1[i] == nums2[j] for j in range(len(nums2))))))
        result.append(list(set(nums2[i] for i in range(len(nums2)) if not any(nums2[i] == nums1[j] for j in range(len(nums1))))))

        return result


        
