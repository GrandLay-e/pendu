# **Projet de Scrapping et Jeu du Pendu**

Ce projet récupère des mots aléatoires à partir d'une source web, puis permet à l'utilisateur de jouer au jeu du **pendu** en essayant de deviner un mot choisi aléatoirement.

---

## **Fonctionnalités :**

1. **Récupération des mots à partir du web** :
   - Les mots sont extraits depuis un site web à l'aide du scrapping.
   - Le projet récupère des mots à partir de l'URL `https://usito.usherbrooke.ca/index/mots/tous/` en scrappant chaque page de lettres de l'alphabet de `a` à `z`.

2. **Expression régulière pour valider les mots** :
   - Seuls les mots contenant entre 5 et 10 caractères alphanumériques sont pris en compte.

3. **Sauvegarde des mots dans un fichier** :
   - Les mots récupérés sont enregistrés dans un fichier texte `words.txt`.

4. **Définition du mot** :
   - Le programme permet de récupérer la définition d'un mot via un autre site web et l'affiche dans la console.

5. **Jeu du Pendu** :
   - Le programme choisit un mot aléatoire du fichier `words.txt` et lance une partie du jeu du pendu.
   - L'utilisateur doit deviner le mot lettre par lettre en fonction du nombre de vies initiales.

---

## **Prérequis** :

Avant de pouvoir utiliser ce programme, assurez-vous que les bibliothèques suivantes sont installées :

- `requests`
- `beautifulsoup4`
- `re`
- `logging`

Pour installer les dépendances nécessaires, vous pouvez utiliser `pip` :

```bash
pip install requests beautifulsoup4
```

---

## **Utilisation** :

### **1. Récupérer un mot et ses définitions** :

Le programme peut être utilisé pour récupérer la définition d'un mot via l'URL d'Usito. Par exemple, pour récupérer les informations d'un mot donné, il suffit d'exécuter le script principal. Lorsque vous êtes invité à saisir un mot, entrez-le et appuyez sur "Entrée". Vous recevrez la définition du mot s'il existe.

```bash
python mots.py
```

Vous serez invité à entrer un mot, et le programme affichera la définition du mot récupéré depuis `https://usito.usherbrooke.ca/`.

### **2. Jouer au jeu du Pendu** :

Lors de l'exécution du jeu, le programme choisit un mot aléatoire parmi les mots récupérés et lance une partie du pendu. Vous devez deviner le mot en saisissant des lettres. Vous avez un nombre de vies basé sur la longueur du mot à deviner.

#### Commandes :
- Vous devez entrer une lettre à la fois pour deviner le mot.
- Si vous devinez une lettre incorrecte, vous perdez une vie.
- Si vous devinez correctement une lettre, elle est révélée dans le mot à deviner.

Le jeu continue jusqu'à ce que vous trouviez le mot ou que vous ayez épuisé toutes vos vies.

---

## **Explication du Code** :

### **1. Fonction `all_words_in_link(link_to_scrap)`** :
   - Cette fonction récupère tous les mots d'une page spécifique à partir d'un lien donné.
   - Elle utilise **requests** pour envoyer une requête HTTP et **BeautifulSoup** pour analyser la page HTML.
   
### **2. Fonction `all_words_in_all_links()`** :
   - Elle génère tous les liens à partir de l'alphabet et récupère les mots valides à partir de chaque lien.

### **3. Fonction `write_words_to_file(words, file)`** :
   - Cette fonction enregistre les mots dans un fichier texte `words.txt`.

### **4. Fonction `getWordDefinition(word)`** :
   - Elle récupère la définition d'un mot à partir du site Usito.

### **5. Fonction `get_word(file)`** :
   - Elle récupère un mot aléatoire depuis le fichier `words.txt`. Si le fichier n'existe pas, il récupère d'abord les mots depuis le web.

### **6. Jeu du Pendu** :
   - Une partie du pendu est lancée avec un mot aléatoire, et l'utilisateur doit deviner ce mot avec un nombre de vies déterminé par la longueur du mot.
   - La partie se termine lorsque l'utilisateur trouve le mot ou épuisé ses vies.

---

## **Logs** :

Le projet génère un fichier `words.log` pour enregistrer les événements et erreurs pendant le scrapping et le processus du jeu du pendu. Les logs incluent les connexions réussies aux pages, les erreurs de requêtes et les erreurs inattendues.

### Exemple de contenu de `words.log` :
```
2025-03-16 14:00:00,000 - INFO - Tentative de connexion à l'URL : https://usito.usherbrooke.ca/index/mots/tous/a
2025-03-16 14:00:01,000 - ERROR - Erreur de requête : [Erreur HTTP]
```

---

## **Améliorations possibles** :

- Ajouter des fonctionnalités pour jouer à plusieurs parties consécutives.
- Intégrer un système de sauvegarde pour suivre les scores du joueur.
- Ajouter une interface graphique pour une meilleure expérience utilisateur.

---

## **License** :

Ce projet est sous la licence MIT. Vous pouvez l'utiliser et le modifier selon vos besoins.
