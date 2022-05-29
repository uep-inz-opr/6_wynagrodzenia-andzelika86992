class Pracownik:
    def __init__(self, imie, wynagrodzenie_brutto):
        self.imie = imie
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def ubezpieczenie_spoleczne(self)->float:
        emerytalna = self.wynagrodzenie_brutto * 0.0976
        rentowa = self.wynagrodzenie_brutto * 0.015
        chorobowa = self.wynagrodzenie_brutto * 0.0245
        return round(emerytalna + rentowa + chorobowa,2)

    def wynagrodzenie_netto(self)->float:
        podstawa = self.wynagrodzenie_brutto - self.ubezpieczenie_spoleczne()
        ubezpiecznie_zdrowotne = podstawa * 0.09
        skladka_ubez_zdrowotne_odliczana_od_podatku = podstawa * 0.0775
        koszt_uzyskania_przychodu = 111.25
        podstawa_obliczenia_zaliczki_na_podtek_dochodowy = round(self.wynagrodzenie_brutto - koszt_uzyskania_przychodu - self.ubezpieczenie_spoleczne())
        zaliczka_na_podatek_dochodowy_przed_obliczeniem_skladki_zdrowotnej = (podstawa_obliczenia_zaliczki_na_podtek_dochodowy * 0.18) - 46.33
        zaliczka_na_podatek_dochodowy_do_pobrania = round(zaliczka_na_podatek_dochodowy_przed_obliczeniem_skladki_zdrowotnej - skladka_ubez_zdrowotne_odliczana_od_podatku)
        return round(self.wynagrodzenie_brutto - self.ubezpieczenie_spoleczne() - ubezpiecznie_zdrowotne - zaliczka_na_podatek_dochodowy_do_pobrania,2)

    def skladki_pracodawcy(self)->float:
        emerytalna = self.wynagrodzenie_brutto * 0.0976
        rentowa = self.wynagrodzenie_brutto * 0.065
        wypadkowa = self.wynagrodzenie_brutto * 0.0193
        fp = self.wynagrodzenie_brutto * 0.0245
        fgsp = self.wynagrodzenie_brutto * 0.001
        return round(emerytalna + rentowa + wypadkowa + fp +fgsp, 2)

    def laczny_koszt_na_pracownika(self)->float:
        return round(self.wynagrodzenie_brutto + self.skladki_pracodawcy(),2)

ilosc = int(input(""))

pracownicy = []
for i in range(0, 2):
    dane = input("".format(i + 1)).split(" ")
    pracownicy.append(Pracownik(dane[0], dane[1]))

laczny_koszt_na_wszytkich_pracownikow = 0
for pracownik in pracownicy:
    print((f"{pracownik.imie} {pracownik.wynagrodzenie_netto():.2f} {pracownik.skladki_pracodawcy():.2f} {pracownik.laczny_koszt_na_pracownika():.2f}"))
    laczny_koszt_na_wszytkich_pracownikow += pracownik.laczny_koszt_na_pracownika()

print(f"{laczny_koszt_na_wszytkich_pracownikow}")