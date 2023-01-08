from oito_rainhas import Queens


def test1():  # Tabuleiro vazio
    t1 = Queens([])
    assert t1.solve() == -1


def test2():  # Sem damas
    t2 = Queens(["00000000", "00000000",
                 "00000000", "00000000",
                 "00000000", "00000000",
                 "00000000", "00000000"])

    assert t2.solve() == -1


def test3():  # Tamanho errado
    t3 = Queens(["00101000", "01000000",
                 "00000010", "01000000",
                 "00000010", "10000000",
                 "00000010"])

    assert t3.solve() == -1


def test4():  # 2 damas na mesma coluna
    t4 = Queens(["10000000", "10000000",
                 "00100000", "01000000",
                 "00000001", "00000010",
                 "01000000", "00001000"])

    assert t4.solve() == 0


def test5():  # 2 damas na mesma linha
    t5 = Queens(["10000001", "00000000",
                 "01000000", "00000100",
                 "00100000", "00000010",
                 "00010000", "00000001"])

    assert t5.solve() == 0


def test6():  # 2 damas na mesma diagonal direita
    t6 = Queens(["10000000", "00000001",
                 "01000000", "00001000",
                 "00010000", "00000010",
                 "00000100", "00100000"])

    assert t6.solve() == 0


def test7():  # Caso correto
    t7 = Queens(["00010000", "00000100",
                 "00000001", "01000000",
                 "00000010", "10000000",
                 "00100000", "00001000"])
    assert t7.solve() == 1


def test8():  # 2 damas na mesma diagonal esquerda
    t8 = Queens(["01000000", "00000001",
                 "10000000", "00001000",
                 "00010000", "00000010",
                 "00000100", "00100000"])

    assert t8.solve() == 0
