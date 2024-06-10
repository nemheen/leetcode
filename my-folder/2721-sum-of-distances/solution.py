class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        n = len(nums)
        out = [0] * n
        pos = defaultdict(list)

        # Store positions of each element
        for i in range(n):
            pos[nums[i]].append(i)

        # Calculate distances using prefix sums
        for indices in pos.values():
            m = len(indices)
            if m > 1:
                # Compute prefix sums of indices
                prefix_sum = [0] * (m + 1)
                for i in range(m):
                    prefix_sum[i + 1] = prefix_sum[i] + indices[i]

                # Calculate sum of distances for each occurrence
                total_sum = prefix_sum[m]
                for i in range(m):
                    left_sum = prefix_sum[i]
                    right_sum = total_sum - prefix_sum[i + 1]
                    left_count = i
                    right_count = m - i - 1

                    out[indices[i]] = (indices[i] * left_count - left_sum) + (right_sum - indices[i] * right_count)

        return out

