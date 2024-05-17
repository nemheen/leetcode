class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(st):
            if st in memo:
                return memo[st]
            if st == len(s):
                return [""]

            curr = []
            for end in range(st+1, len(s)+1):
                word = s[st:end]

                if word in word_set:
                    for suffix in dfs(end):
                        if suffix:
                            curr.append(word+" "+suffix)
                        else:
                            curr.append(word)
            memo[st] = curr

            return curr

        return dfs(0)
            
        return fun(s, word_set, {})
