from reglog1 import *
k = ["kasutaja1",]
s = ["salasõna1",]
sõna = ["auto",]
while True:
    try:
        Lll=int(input("vali üks viiest funktsioonist\n"
        "1. Registreerimine\n"
        "2. Autoriseerimine\n"
        "3. Muuda unustatud parool\n"
        "4. Muuda nimi või parool\n"
        "5. lõppetamine\n"
        ))
        break
    except:
        print("sisestage 1-5")
if Lll == 1:
    reg()