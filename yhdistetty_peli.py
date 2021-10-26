import main
import kysymyspeli


def suorita():
    while True:
        vastaus = int(input("Haluatko pelata peliä 1 vai 2? Paina 0 lopettaaksesi"))
        if vastaus == 1:
            main.peli()
        elif vastaus == 2:
            kysymyspeli.peli2()
        elif vastaus == 0:
            break
suorita()