from reglog1 import *
while True:
    Lll=int(input("vali üks viiest funktsioonist\n"
    "1. Registreerimine\n"
    "2. Autoriseerimine\n"
    "3. Muuda unustatud parool\n"
    "4. Muuda nimi või parool\n"
    "5. lõppetamine\n"
    "6. (admin)kõigi loendite kontrollimine\n"
    ))
    if Lll == 1:
        reg(k, s, sõna)
    elif Lll == 2:
        log(s, k)
    elif Lll == 3:
        muudaP(s, k)
    elif Lll == 4:
        muuda(k, s)
    elif Lll == 5:
        print("Nägemist")
        break
    elif Lll == 6:
        print(k, s, sõna)
    else:
        print("Sisestage õige vastus")