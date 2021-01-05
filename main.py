from autok import autok
from typing import List


def main() -> None:

    autok_adatok: List[autok] = []
    with open('forras.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            autok_adatok.append(autok(sor))

    #  Hány db autó szerepel a listában?
    print(f'{len(autok_adatok)} db autó szerepel a listában\n')

    #  Hány db Ford által gyártott jármű van a listában?
    ford_gyarto: int = 0
    for ford in autok_adatok:
        if ford.gyarto == 'Ford':
            ford_gyarto += 1
    print(f'Ebből {ford_gyarto} db Ford típusú jármű\n')

    #  Melyik autónak van a legnagyobb lökettérfugatú motorja?
    #  Segítség: a motorcm3 adatot kell felhasználni a számítás során (maximum érték keresés)
    legnagyobb_cm3: autok = autok_adatok[0]
    for i in autok_adatok[1:]:
        if i.motorcm3 > legnagyobb_cm3.motorcm3:
            legnagyobb_cm3 = i
    print(f'A legnagyobb lökettérfogatú autó: {legnagyobb_cm3.gyarto} {legnagyobb_cm3.tipus} {legnagyobb_cm3.motorcm3}cm3 hengerűrtartalommal\n')

    #  benzines és dízel autók száma
    benzines: int = 0
    for benzin in autok_adatok:
        if benzin.uzemanyag == 'benzin':
            benzines += 1
    # A dízeles autók számát meglehet adni úgy is, hogy az autók számából kivonjuk a benzines autók számát
    # dizeles: int = 0
    # for dizel in autok_adatok:
        # if dizel.uzemanyag == 'dízel':
            # dizeles += 1
    # print(f'{benzines} db benzines és {dizeles} db dízeles autó van a listában')
    print(f'{benzines} db benzines és {len(autok_adatok) - benzines} db dízeles autó van a listában\n')

    #  A leggyengébb autó adatai
    legkisebb_le: autok = autok_adatok[0]
    for j in autok_adatok[1:]:
        if j.motorle < legkisebb_le.motorle:
            legkisebb_le = j
    print(f'A leggyengébb autó: {legkisebb_le.gyarto} {legkisebb_le.tipus} {legkisebb_le.motorle} lóerővel')

    legnagyobb_le: autok = autok_adatok[0]
    for k in autok_adatok[1:]:
        if k.motorle > legnagyobb_le.motorle:
            legnagyobb_le = k
    print(f'A legerősebb autó: {legnagyobb_le.gyarto} {legnagyobb_le.tipus} {legnagyobb_le.motorle} lóerővel\n')

    # Eldöntés tétele, van-e Suzuki a listában?
    van_suzuki: bool = False
    for s in autok_adatok:
        if s.gyarto == 'Suzuki':
            van_suzuki = True
            break
    print(f'{"Van" if van_suzuki else "Nincs"} Suzuki a listában')

    # Eldöntés tétele bekért input adat alapján
    print('Kérem adjon meg egy autó márkát pl.: Opel (szerepel a listában), vagy Renault (nem szerepel a listában)')
    # Input mezőt nem ártana még ellenőrizni, mert üres értéket is elfogad
    auto_input = str(input("Autómárka: "))
    van_auto: bool = False
    for a_input in autok_adatok:
        if a_input.gyarto == auto_input:
            van_auto = True
            break
    print(f'{"Van" if van_auto else "Nincs"} {auto_input} a listában\n')

    #  Megszámlálás tétele
    #  Hány olyan autó van a listában, aminek a végsebessége eléri a 190 km/h-t?
    vegsebesseg: int = 0
    for sebesseg in autok_adatok:
        if sebesseg.vegsebesseg >= 200:
            vegsebesseg += 1
    print(f'A listában szereplő autók közül {vegsebesseg} db tud legalább 200 km/h sebességgel haladni\n')

    # Összegzés tétele. Határozzuk meg az öttel osztható motornyomaték értékek számát és átlagát
    db_oszt5: int = 0
    osszeg_oszt5 = 0
    for oszt in autok_adatok:
        if oszt.motornyomatek % 5 == 0:
            db_oszt5 += 1
            osszeg_oszt5 += oszt.motornyomatek
    if db_oszt5 == 0:
        print('Nincs a listában öttel osztható nyomaték érték')
    else:
        print(f'Az öttel osztható nyomaték értékek darabszáma: {db_oszt5}')
        print(f'Az összegük: {osszeg_oszt5} és az átlaguk kerekített értéke: {int(osszeg_oszt5 / db_oszt5)}')

    # Írjuk ki fájlba a 7 személyes autók adatait
    szemely_7: autok = autok_adatok[0]
    for szemely in autok_adatok[1:]:
        if szemely.utasokszama == 7:
            szemely_7 = szemely
    #  Sajnos csak egy autót ír be a fájlba, miközben van több is. :(
    with open('autok7.txt', 'w', encoding='utf-8') as file2:
        file2.writelines(str(szemely_7.gyarto + ' ' + szemely_7.tipus))


if __name__ == "__main__":
    main()
