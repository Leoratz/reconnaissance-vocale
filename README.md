# 🗣️ Assistant Vocal Python

Un assistant vocal simple développé en Python qui permet de contrôler des actions de ton ordinateur à l'aide de commandes vocales. Le projet utilise des technologies telles que speech recognition, text-to-speech, et des commandes système pour interagir avec l'utilisateur.

## Fonctionnalités

* **Reconnaissance vocale** : L'assistant comprend et interprète les commandes vocales.
* **Commandes possibles** :
    * **Ouvrir le navigateur** : L'Assistant ouvre Google dans le navigateur par défaut.
    * **Recherche vocale sur Google** : L'utilisateur peut dicter une recherche, et l'Assistant ouvre Google avec cette recherche.
    * **Affichage de l'heure et de la date** : L'Assistant peut dire l'heure ou la date actuelle.
    * **Verrouillage de l'écran** : L'Assistant verrouille l'ordinateur.
* **Texte à voix** : L'Assistant répond vocalement aux utilisateurs avec pyttsx3.

<hr>

## 📦 Installation

1. Cloner ce projet :

````bash
git clone https://github.com/Leoratz/reconnaissance-vocale.git
cd reconnaissance-vocale
````

2. Installer les dépendances :

````bash
pip install -r requirements.txt
````
<hr>

## ⚙️ Fichiers principaux

1. ````main.py```` :
Contient la logique principale de l'assistant vocal. Il écoute les commandes vocales, traite les commandes et effectue les actions correspondantes.

2. ````commands.py```` :
Contient toutes les fonctions qui exécutent les actions liées aux commandes vocales, comme ouvrir un navigateur, dire l'heure, verrouiller l'écran, etc.

3. ````requirements.txt```` :
Liste toutes les dépendances nécessaires pour faire fonctionner le projet.

<hr>

## 🛠️ Dépendances

* **speechrecognition** : Utilisé pour la reconnaissance vocale.
* **pyttsx3** : Utilisé pour la conversion du texte en voix (synthèse vocale).
* **pyaudio** : Nécessaire pour l'enregistrement audio à partir du microphone.
* **webbrowser** : Utilisé pour ouvrir des pages web dans le navigateur.
* **subprocess** : Utilisé pour exécuter des commandes système, comme verrouiller l'écran ou ouvrir un navigateur.

<hr>

## 🚀 Exécution du Projet

1. Assure-toi d'avoir configuré ton microphone.

2. Lance le programme avec la commande suivante :

    ````bash
    python main.py
    ````

3. Une fois lancé, dis des commandes comme :
    * "Ouvre navigateur" : L'Assistant ouvrira Google.
    * "Donne-moi l'heure" : L'Assistant te dira l'heure actuelle.
    * "Donne-moi la date" : L'Assistant te dira la date du jour.
    * "Verrouille l'écran" : L'Assistant verrouillera ton ordinateur.

<hr>

## 📝 Auteurs

Créateurs et contributeurs :
* [Léora CHRIQUI](https://github.com/Leoratz) 
* [Antoine SCHMERBER-PERRAUD](https://github.com/AntoineSP01)
* [Alyssia LORSOLD PRADON](https://github.com/alyssialopr)