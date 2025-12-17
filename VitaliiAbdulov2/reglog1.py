import random
k = ["kasutaja1",]
s = ["salasõna1",]
sõna = ["auto",]
#reg
def reg():
    while True:
                N = input("Sisetage nimi: ")
                if N in k:
                    print("vale nimi palun sisesta oõige nimi")
                else:
                    break
    REGIS = input("kas sa tahad luua parool (jah/ei):" )
    if REGIS == "jah":
        P = input("Sisetage parool: ")         
        k.append(N)
        s.append(P)
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
def log():
    while True:
        N = input("Sisetage nimi: ")
        P = input("Sisetage parool: ")
        if_autoriseeritud = False
        if N in k and P in s:
            if_autoriseeritud = True
            break
        else: 
            print("vale parool või nimi")
#muuda unustatud parool
def muudaP():
    while True:
        N = input("Sisetage nimi: ")
        SS = input("Sisetage proovisõna: ")
        if N in k and SS in sõna:
            uusparool = input("Sisestage uus parool: ")
            s.append(uusparool)
            break
        else:
            print("vale nimi või proovisõna")   
#muuda parool ja nimi
def muuda():
    while True:
        N = input("Sisetage nimi: ")
        if N in k:
            P = input("Sisestage parool: ")
            if P in s:
                SS = input("Sisetage proovisõna: ")
                break
        if N in k and P in s and SS in sõna:
            T = input("mis sa tahad muuda Parool või Nimi (P/N): ")
            if T == "P":
                uusparool = input("Sisestage uus parool: ")
                break
            elif T == "N":
                uusnimi = input("Sisetage uus nimi")
                break
            else:
                print("kirjuta P või N!!!")
        else:
            print("Vale nimi, parool või proovisõna")