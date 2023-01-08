class Queens:
    def __init__(self, board):
        self.board = board

    def checkColumn(self):  # Checa se há mais de 1 dama por coluna
        for num in range(8):
            countQueens = 0
            for i in self.board:
                if i[num] == "1":
                    countQueens += 1
            if countQueens > 1:
                return -1
        return 1

    def solve(self):
        countQueens = 0
        countSize = 0
        # if self.board == []:
        #     return -1
        for i in self.board:
            countQueens += i.count("1")
            countSize += 1
        if countQueens != 8 or countSize != 8:
            return -1
        if self.checkColumn() == -1:
            return -1
