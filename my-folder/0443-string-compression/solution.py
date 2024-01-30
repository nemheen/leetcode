class Solution:
    def compress(self, chars: List[str]) -> int:
        wr = 0
        rd = 0

        while rd < len(chars):
            ch = chars[rd]
            k = 0

            while rd < len(chars) and chars[rd] == ch:
                rd += 1
                k += 1
            chars[wr] = ch
            wr += 1

            if k > 1:
                for d in str(k):
                    chars[wr] = d
                    wr += 1

            

        return wr





        
