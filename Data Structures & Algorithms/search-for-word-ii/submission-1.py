class Trienode:
    def __init__(self): 
        self.children = {}
        self.isword = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.isword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trienode()

        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if (r<0 or c<0 or r>= rows
             or c >= cols or board[r][c] not in node.children or   (r,c) in visit):
                return False 
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)
            dfs(r+1,c, node, word)
            dfs(r,c+1, node, word)
            dfs(r-1,c, node, word)
            dfs(r,c-1, node, word)
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")

        return list(res)
        

        
