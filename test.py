def checkDiagRight(board):
    diags = []
    for row in range(8):
        for col in range(8):
            p = board[row][col]
            if p == "1":
                diags.append((row - col, p))
    print(diags)
    print(set(diags))
    if len(diags) == len(set(diags)):
        return 1
    else:
        return -1


print(checkDiagRight(["00010000", "00000100",
                      "00000001", "01000000",
                      "00000010", "10000000",
                      "00100000", "00001000"]))
