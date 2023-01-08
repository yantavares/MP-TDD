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
