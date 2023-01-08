from oito_rainhas import Queens


def test1():  # Tabuleiro vazio
    t1 = Queens([])
    assert t1.solve() == -1


def test2():  # Sem damas
    t2 = Queens(["00000000", "00000000",
                 "00000000", "00000000",
                 "00000000", "00000000",
                 "00000000", "00000000"])
