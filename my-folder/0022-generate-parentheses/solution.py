class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

      out = []

      def dfs(p, l, r, out):
        if l:
          dfs(p+'(', l-1, r, out)
        if r>l:
          dfs(p+')', l, r-1, out)
        if not r:
          out.append(p)
        return out
      
      return dfs('', n, n, out)

