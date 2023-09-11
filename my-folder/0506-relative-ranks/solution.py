class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        ans = [" "]*n
        d = defaultdict(int)
        for i, k in enumerate(score):
            d[k] = i

        score.sort(reverse=True)
     
        for i in range(n):
            if i==0:
                ans[d[score[i]]] = "Gold Medal"
            elif i == 1:
                ans[d[score[i]]] = "Silver Medal"
            elif i==2: 
                ans[d[score[i]]] = "Bronze Medal"
            else:
                ans[d[score[i]]] = str(i+1)
            
        return ans
        
