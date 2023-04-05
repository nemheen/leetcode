class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=''
        if len(num1)==0 or len(num2)==0:
            return res
        if num1[0]=='0' or num2[0]=='0':
            return '0'


        x, y, z = 0, 0, 0
        for num in num1:
            x=x*10+(ord(num)-ord('0'))
        for num in num2:
            y=y*10+(ord(num)-ord('0'))

        z=x*y
        
        # while z:
        #    res += chr((z % 10) + ord('0'))
        #    z=z/10

        while z:
            res = res +(chr(ord('0') + z % 10)) 
            z //= 10 
       
       
        return res[::-1]
