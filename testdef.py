
import mots
try:
    with open("words.txt", 'r', encoding='utf-8') as f:
        words = f.readlines()
    trouve = 0
    introuve = 0
    for mot in words:
        defin = mots.getDef(mot)
        if len(defin) > 0 and defin[0] != "Pas de définition trouvée pour ce mot":
            trouve += 1
            print(f"{mot.replace("\n","")} \t\t: ✅")
        else:
            introuve += 1
            print(f"{mot.replace("\n","")} \t\t: ❌")

    print(f"Nombre de mots trouvés : {trouve}")
    print(f"Nombre de mots introuvés : {introuve}")

except KeyboardInterrupt:
    print("Quitté !")