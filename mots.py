# Récupérer les mots à partir du web. Au moins 15 mots et en choisir un par hasard
# SCRAPPING

import requests
from bs4 import BeautifulSoup
import re
import logging
from pprint import pprint
from time import sleep

# Expression régulière pour vérifier les mots valides
BONMOT = r"^[A-Za-zÀ-Üà-ü]{5,}$"
# Alphabet pour générer les liens
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# URL de base pour le scrapping
url_base = "https://usito.usherbrooke.ca/index/mots/tous/"

# Configuration du logging
logging.basicConfig(filename='words.log', 
                    filemode = 'w',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

# Générer tous les liens à partir de l'alphabet
all_links = [url_base+l for l in alphabet]

# Fonction pour récupérer tous les mots d'un lien
def all_words_in_link(link_to_scrap):
    all_words = []
    with requests.Session() as session:
        try:
            logging.info(f"Tentative de connexion à l'URL : {link_to_scrap}")
            result = session.get(link_to_scrap)
            result.raise_for_status()
            
            logging.debug("Requête réussie, traitement du contenu HTML...")
            soup = BeautifulSoup(result.text, 'html.parser')
            allWordsInLink = soup.select(".entrées li a")
            all_words = [words_link.get_text() for words_link in allWordsInLink]
            logging.info(f"Nombre de mots trouvés : {len(all_words)}")
            
        except requests.RequestException as e:
            logging.error(f"Erreur de requête : {e}")
        except Exception as e:
            logging.critical(f"Erreur inattendue : {e}")

    return all_words

# Fonction pour récupérer tous les mots de tous les liens
def all_words_in_all_links():
    words = []
    for link in all_links:
        words.extend([word.strip() for word in all_words_in_link(link) if re.match(BONMOT, word)])
    return words

# Fonction pour écrire les mots dans un fichier
def write_words_to_file(words, file = "words.txt"):
    with open(file,"w", encoding='utf-8') as f:
        f.write("\n".join(words))

# Fonction pour obtenir la définition d'un mot
def getWordDefinition(word):
    definition = []
    link = "https://usito.usherbrooke.ca/définitions/" + word.lower().strip()
    with requests.Session() as session:
        try:
            result = session.get(link)
            result.raise_for_status()
            soup = BeautifulSoup(result.text, 'html.parser')
            definition_elements = soup.select(".def_sous_entree-style")
            definition = [d.get_text() for d in definition_elements]
        except requests.RequestException as e:
            logging.error(f"Erreur de requête : {e}")
        except Exception as e:
            logging.critical(f"Erreur inattendue : {e}")
    return definition

def getDef(word):
    definition = getWordDefinition(word)
    if len(definition) == 0:
        i = 1
        for suffix in ["_1","_2", "_3"]:
            tempdef = getWordDefinition(word + suffix)
            logging.info("Autres tentatives avec les homonymes !")
            if len(tempdef) > 0:
                logging.info(f"{i}e homonyme trouvé")
                definition.append(f"{i}e definition \n")
                definition.extend(tempdef)
                i+=1
            else:
                logging.info(f"{i}e homonyme non trouvé ! ")
        if len(definition) == 0:
            logging.info(f"Pas de définition trouvée pour le mot {word}")
            definition.append("Pas de définition trouvé pour ce mot")
    return definition

if __name__ == "__main__":
    mot = input("mot : ")
    definition = getDef(mot)
    pprint(definition)
