from reglog2 import *
#reg
def reg():
    N = input("Sisetage nimi: ")
    P = input("Sisetage parool: ")
    SS = input("Sisestage sõna: ")
    if N in k:
        print("vale nimi palun sisesta oõige nimi")
    else:
        k.append(N)
        s.append(P)
#log
def log():
    N = input("Sisetage nimi: ")
    P = input("Sisetage parool: ")
    if_autoriseeritud = False
    while True:
        if N in k and P in k:
            if_autoriseeritud = True
            break
        else: 
            print("vale parool või nimi")
#muuda unustatud parool
def muudaP():
    N = input("Sisetage nimi: ")
    SS = input("Sisetage proovisõna: ")
    if N in k and SS in sõna:
        uusparool = input("Sisestage uus parool: ")
        s.append(uusparool)
    else:
        print("vale nimi või proovisõna")   
#muuda parool ja nimi
def muuda():
    N = input("Sisetage nimi: ")
    P = input("Sisestage parool: ")
    SS = input("Sisetage proovisõna: ")
    if N in k and P in s and SS in sõna:
        T = input("mis sa tahad muuda P või N")
        if T == "P":
            uusparool = input("Sisestage uus parool: ")
        elif T == "N":
            uusnimi = input("Sisetage uus nimi")
        else:
            print("kirjuta P või N!!!")
    else:
        print("Vale nimi, parool või proovisõna")
#lõpetamine
# def lõpp():
#     Lõpp1 = input("Kas sa tahad välja? (ei/jah): ")
#     if Lõppp1 == "jah":
#     print("Nägemist!")
    