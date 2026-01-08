def kirjuta_failisse(failinimi:str,loend:list):
    while True:
        reziim=input("Seseta faili avamise reziim (w - kirjutamine, a - lisamine): ")
        if reziim not in ["w", "a"]:
            print("Vale reziim!")
        else:
            break
    for i in range(10):
        element=input("sisesta tekst/info: ")
        loend.append(f"{element}\n")
    with open(failinimi, reziim, encoding="utf-8") as f:
        #f.writelines(loend)
        #või for rida in loend: f.write(rida)
        for rida in loend:
            f.write(rida+"\n")
def loe_failist(failinimi:str)->list:
    loend=[]
    with open(failinimi+".txt", "r", encoding="utf-8") as f:
        for rida in f:
            loend.append(rida.strip())
    return loend



loend=["Rida 1", "Rida 2"]
failinimi=input("Sisesta faili nimi: ")
kirjuta_failisse(failinimi, loend)