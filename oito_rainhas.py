class Queens:
    def __init__(self, board):
        self.board = board

    def checkColumn(self) -> bool:  # Checa se há mais de 1 dama por coluna
        for num in range(8):
            countQueens = 0
            for i in self.board:
                if i[num] == "1":
                    countQueens += 1
            if countQueens > 1:
                return False
        return True

    def checkRows(self) -> bool:  # Checa se há mais de 1 dama por linha
        for i in self.board:
            if i.count("1") > 1:
                return False
        return True

    def checkDiagRight(self) -> bool:
        diags = []
        for row in range(8):
            for col in range(8):
                p = self.board[row][col]
                if p == "1":
                    diags.append((row - col, p))
        if len(diags) == len(set(diags)):
            return True
        else:
            return False

    def checkDiagLeft(self) -> bool:
        diags = []
        for row in range(8):
            for col in range(8):
                p = self.board[row][col]
                if p == "1":
                    diags.append((row + col, p))
        if len(diags) == len(set(diags)):
            return True
        else:
            return False

    def checkAll(self) -> int:
        if self.checkColumn() and self.checkRows() and self.checkDiagRight() and self.checkDiagLeft:
            return 1
        else:
            return -1

    def solve(self) -> int:
        if self.board == []:
            return -1
        countQueens = 0
        countSize = 0
        for i in self.board:
            countQueens += i.count("1")
            countSize += 1
        if countQueens != 8 or countSize != 8:
            return -1
        return self.checkAll()


if __name__ == '__main__':
    def makeBoard():
        board = []
        try:
            for i in range(8):
                b = input()
                board.append(b)
        except:
            board = []

    def run():
        b = makeBoard()
        board = Queens(b)
        return board.solve()

    run()
