import os
from random import randint
from pathlib import Path

import mots

# Récupèration d'un mot aléatoire dans le fichier wrods.txt
# S'il n'existe pas on le crée en récupèrant les mots depuis le web
def get_word(file):
    if Path(file).exists():
        with open(file, 'r', encoding='utf-8') as f:
            words = f.readlines()
            return words[randint(0, len(words) -1)].strip().upper()
    else:
        print("Fichier introuvable, récupération des mots depuis le web...")
        mots.write_words_to_file(mots.all_words_in_all_links(), file)
        return get_word(file)

# Initialisation des variables
file = "words.txt"
word = get_word(file)
definitions = mots.getWordDefinition(word)
trouve = bool()

vies = len(word) + len(word)//2
mot_en_cours = ["*" for l in word ]

print("Bienvenue dans le jeu du pendu !")
print(f"Nombre de vies : {vies * '❤️ '} ({vies})")
print("".join(mot_en_cours))

# Boucle principale 
while trouve == False or vies > 0:
    lettre = ""

    #Saisie d'une lettre, et uniquement une lettre
    while len(lettre.strip())!=1:
        lettre = input("Saisissez une lettre pour trouver le mot : ").upper()
        #os.system('clear') # Sous linux
        os.system('cls') #Sous windows
    
    #Vérifier que c'est bien une lettre (pas de chiffre ou autres)
    if lettre.isalpha():
        if lettre not in word:
            vies -=1
            print(f"Raté ❌ \n {"".join(mot_en_cours)} \n Nombre de vies : {vies * "❤️ "} ({vies})")
        else:
            i=0
            while i< len(word):
                if lettre == word[i]:
                    mot_en_cours[i] = lettre
                i+=1
            print("Lettre touvé ✅ : ", "".join(mot_en_cours), f"\n Nombre de vie : {vies * "❤️ "} ({vies})")
    else:
        print("Veuillez saisir une lettre SVP ! ")

    #S'il trouve le mot
    if "".join(mot_en_cours) == word:
        print("🎊 Mot trouvé", "".join(mot_en_cours),"Félicitations ! 🎊 \n")
        trouve = True
        break

    #Fin des tentatives sans trouver le bon mot
    if vies < 1 and trouve == False:
        print(f"PERDU ! 💔, Vies : 0 \n Le mot à Déviner était : {word}")
        break
#Afficher le score dans tous les cas
print(f" Score : {vies * 5} 🏆")

#Ainsi que le définition du mot (s'il est trouvé)
print("Définition(s) du mot : ")
i = 1
for definition in definitions:
    print(f"{i} - {definition}")
    i+=1
print("Fin du jeu !")