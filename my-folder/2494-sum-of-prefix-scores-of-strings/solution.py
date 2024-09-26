class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.count = 0      # Count of how many words pass through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment the count for this prefix
    
    def get_prefix_score(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.count  # Add count at each node for the prefix score
            else:
                break
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Step 1: Build a Trie from all the words
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # Step 2: Calculate the prefix score for each word
        result = []
        for word in words:
            score = trie.get_prefix_score(word)
            result.append(score)
        
        return result

