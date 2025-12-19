import random
k = ["kasutaja1", "nimi2"]
s = ["salasõna1", "parool2"]
sõna = ["auto1", "sõna2"]
#reg
def reg(k, s, sõna):
    while True:
        N = input("Sisetage nimi: ")
        if N in k:
            print("vale nimi palun sisesta oõige nimi")
        else:
            k.append(N)
            break
    REGIS = input("kas sa tahad luua parool (jah/ei):" )
    if REGIS == "jah":
        Par = input("Sisetage parool: ")         
        s.append(Par)
    elif REGIS == "ei":
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0 + str1 + str2 + str3
        ls = list(str4)
        random.shuffle(ls)
        # Eemaldame nimekirjast 12 juhuslikku väärtust (Algselt: Извлекаем из списка 12 произвольных значений)
        psword = ''.join([random.choice(ls) for x in range(12)])
        # Parool on valmis (Algselt: Пароль готов)
        print(psword)
        s.append(psword)
    else:
        print("Sisestage õige vastus(jah/ei)!")
    SS = input("Sisestage sõna: ")
    sõna.append(SS)
#log
def log(s, k):
    while True:
        N = input("Sisetage nimi: ")
        Par = input("Sisetage parool: ")
        if_autoriseeritud = False
        if N in k and s[k.index(N)] == Par:
            if_autoriseeritud = True
            print("Olete oma kontole edukalt sisse loginud.")
            break
        else: 
            print("vale parool või nimi")
#muuda unustatud parool
def muudaP(s, k):
    while True:
        N = input("Sisetage nimi: ")
        SS = input("Sisetage proovisõna: ")
        if N in k and sõna[k.index(N)]:
            uusparool = input("Sisestage uus parool: ")
            indeksp = k.index(N)
            s[indeksp] = uusparool
            break
        else:
            print("vale nimi või proovisõna")
    return(k, s)
#muuda parool ja nimi
def muuda(k, s):
    while True:
        N = input("Sisetage nimi: ")
        Par = input("Sisestage parool: ")
        if N in k and s[k.index(N)] == Par:
            T = input("mis sa tahad muuda Parool või Nimi (P/N): ")
            if T == "P":
                uusparool = input("Sisestage uus parool: ")
                indeksp = k.index(N)
                s[indeksp] = uusparool
                break
            elif T == "N":
                uusnimi = input("Sisetage uus nimi: ")
                indeksn = s.index(Par)
                k[indeksn] = uusnimi
                break
            else:
                print("kirjuta P või N!!!")
        else:
            print("Sisestage õige nimi ja parool")