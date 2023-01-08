class Queens:
    def __init__(self, board):
        self.board = board

    def solve(self):
        countQueens = 0
        countSize = 0
        if self.board == []:
            return -1
        for i in self.board:
            countQueens += i.count("1")
            countSize += 1
        if countQueens != 8 or countSize != 8:
            return -1
