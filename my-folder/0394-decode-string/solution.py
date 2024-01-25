class Solution:
    def decodeString(self, s: str) -> str:
        curr = ""
        st = []
        k = 0
        
        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == "[":
                st.append(k)
                st.append(curr)
                k = 0
                curr = ""
            elif c == "]":
                prev_str = st.pop()
                prev_num = st.pop()
                curr = prev_str + curr * prev_num
            else:
                curr += c
        return curr
        
            



