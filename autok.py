from typing import List


class autok(object):
    gyarto: str
    tipus: str
    uzemanyag: str
    motorcm3: int
    motorle: int
    motornyomatek: int
    vegsebesseg: int
    gyorsulas: float
    sebessegvalto: int
    vegyesfogyasztas: float
    utasokszama: int

    def __init__(self, sor: str) -> None:
        a: List[str] = sor.split(';')
        self.gyarto = a[0]
        self.tipus = a[1]
        self.uzemanyag = a[2]
        self.motorcm3 = int(a[3])
        self.motorle = int(a[4])
        self.motornyomatek = int(a[5])
        self.vegsebesseg = int(a[6])
        self.gyorsulas = float(a[7])
        self.sebessegvalto = int(a[8])
        self.vegyesfogyasztas = float(a[9])
        self.utasokszama = int(a[10])
