# -*- coding:utf-8 -*-
'''
矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，
在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

example1:
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

example2:
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

解：首先遍历找到第一个匹配的点，再从它的上下左右找匹配的点。
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.DFS(board, word, i, j, 0):
                        return True
        return False


    def DFS(self, board, word, i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        temp, board[i][j] = board[i][j], '/'
        res = self.DFS(board, word, i+1, j, k+1) or self.DFS(board, word, i-1, j, k+1) or self.DFS(board, word, i, j+1, k+1) or self.DFS(board, word, i, j-1, k+1)
        board[i][j] = temp
        return res



if __name__ == '__main__':
    a = Solution()
    print (a.exist([["A","B","C","E"],["S","F","B","S"],["A","D","E","E"]], 'SFBS'))

