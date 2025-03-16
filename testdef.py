import mots

with open("words.txt", 'r', encoding='utf-8') as f:
    words = f.readlines()
trouve = 0
introuve = 0
for mot in words:
    if len(mots.getWordDefinition(mot)) > 0 and mots.getWordDefinition(mot)[0] != "Pas de définition trouvée":
        trouve += 1
        print(f"{mot.replace("\n","")} \t\t: ✅")
    else:
        introuve += 1
        print(f"{mot.replace("\n","")} \t\t: ❌")

print(f"Nombre de mots trouvés : {trouve}")
print(f"Nombre de mots introuvés : {introuve}")