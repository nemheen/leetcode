class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        out = ""
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i>=0:
                carry += int(a[i]) 
                i -= 1
            if j>=0:
                carry += int(b[j])
                j -= 1
            out += str(carry%2)
            carry //= 2

        return out[::-1]

        

            


        
