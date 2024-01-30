class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        d, r = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        while d and r:
            dt = d.popleft()
            rt = r.popleft()

            if rt < dt:
                r.append(dt + len(s))
            else: d.append(rt + len(s))

        return 'Radiant' if r else 'Dire' 
            


        
