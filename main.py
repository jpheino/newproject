def peli1():
    kysymykset =[
    "Mistä gcp on lyhenne? \nA: Google Computing Platform \nB: Google Cloud Platform \nC: Google Customer Platform",
    "Mistä tietää millä käyttäjällä operoit? \nA: whoami \nB: whereami \nC: whenami",
    "Mikä näistä virtuaalikonetyypeistä soveltuu parhaiten intensiivisiin prosessointitöihin? \nA: M2 \nB: E2 \nC: C2"
    ]
    maksimi_pisteet = len(kysymykset)
    #tulostaa ohjeet kysymyspelin pelaamiseen
    def ohje():
        print("Ohjelmassa voit valita joko 0 tai 1, 0 lopettaa pelin ja 1 jatkaa peliä.")

    def pelaa():
        i = 0
        pisteet = 0
        for kysymys in kysymykset:
            try:
                vastaus = str(input(f"\n{kysymys}\n>"))
            except ValueError:
                print("Virheellinen komento")
            if i == 0:
                if vastaus.lower() == "b":
                    print("Oikein! Sait yhden pisteen")
                    pisteet += 1
                else:
                    print("Väärin!")
            elif i == 1:
                if vastaus.lower() == "a":
                    print("Oikein! Sait yhden pisteen")
                    pisteet += 1
                else:
                    print("Väärin!")
            elif i == 2:
                if vastaus.lower() == "c":
                    print("Oikein! Sait yhden pisteen")
                    pisteet += 1
                else:
                    print("Väärin!")
            i += 1
        print(f"Sait {pisteet}/{maksimi_pisteet} pistettä!")

    #while-loop joka kutsuu kysymyksentulostusta, käsittelee pelaajan syötteen
    #1 pelaa 0 lopeta
    def suorita():
        ohje()
        while True:
            print()
            kysymys = int(input("Oletko valmis pelaamaan? 1 = Pelaa, 0 = Lopeta "))
            if kysymys == 1:
                pelaa()
            elif kysymys == 0:
                break
            else:
                ohje()

    suorita()

    print("Kiitos pelaamisesta!")




# Tästä lähtee meidän superhieno kyssäripeli


def peli2():

    pisteet = 0
    aloitatko = str(input("Paina 'k' jos haluat aloittaa: "))

    if aloitatko == "k":
        while True:
            print("Vastaa k tai e, mikä tahansa muu lopettaa.")

            kysymys1 = input("Onko Thaikuissa kivaa (k/e): ")
            if kysymys1 == "k":
                print("Oikein!")
                pisteet += 1
            elif kysymys1 == "e":
                print("Väärin!")
            else:
                break

            kysymys2 = input("Onko C# parempi kuin Python (k/e): ")
            if kysymys2 == "e":
                print("Oikein!")
                pisteet += 1
            elif kysymys2 == "k":
                print("Väärin!")
            else:
                break

            kysymys3 = input("Onko GCP parasta ikinä (k/e): ")
            if kysymys3 == "k":
                print("Oikein!")
                pisteet += 1
            elif kysymys3 == "e":
                print("Väärin!")
            else:
                break

    print(f"Sait {pisteet} pistettä!")


if __name__ == "__main__":
    print("Tervetuloa kysymyspeliin!")
    syote = input("Haluatko pelata peliä 1 vai 2?: ")
    if syote == "1":
        peli1()
    elif syote == "2":
        peli2()
    else:
        print("Väärä syöte.. anna numerot 1 tai 2!")

