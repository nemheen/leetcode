class Solution:
    def isCircularSentence(self, s: str) -> bool:
        abc = list(s.split())
        first = abc[0][0]
        end = abc[0][-1]

        if len(s)==1:
            return first==end

        for i in range(1, len(abc)):
            
            st = abc[i][0]

            if not st == end:
                return False
            
            end = abc[i][-1]
            
        if not first==end:
            return False

        return True

