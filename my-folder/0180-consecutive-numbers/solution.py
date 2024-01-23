import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    nums = logs['num']
    consecutiveNums = set()
    i = 1

    while i < len(nums)-1:
        if nums[i-1]==nums[i]==nums[i+1]:
            consecutiveNums.add(nums[i])
            i = i+3
        elif nums[i] != nums[i+1]:
            i = i +2
        elif nums[i-1] != nums[i]:
            i += 1
        
    return pd.DataFrame({"ConsecutiveNums":list(consecutiveNums)})

