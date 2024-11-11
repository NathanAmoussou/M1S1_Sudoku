# Guide d'Utilisation du Solveur de Sudoku

## Introduction

Ce projet est un **solveur de Sudoku** développé en Python, capable de résoudre des grilles de différentes difficultés en appliquant jusqu'à quatre règles de déduction. Il évalue également le niveau de difficulté de la grille en fonction des règles utilisées pour la résoudre. Ce guide vous expliquera comment installer, exécuter et utiliser le programme.

## Table des Matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution du Programme](#exécution-du-programme)
- [Utilisation](#utilisation)
  - [Entrer une Grille](#entrer-une-grille)
  - [Résolution de la Grille](#résolution-de-la-grille)
  - [Interaction Utilisateur](#interaction-utilisateur)
- [Fonctionnalités](#fonctionnalités)
- [Exemples](#exemples)
- [Dépannage](#dépannage)
- [Conclusion](#conclusion)

## Prérequis

- **Python 3.x** : Assurez-vous que Python 3 est installé sur votre système. Vous pouvez vérifier en exécutant `python3 --version` dans votre terminal. Pour ce projet Python 3.9.2 a été utilisé.

## Installation

1. **Cloner le Répertoire du Projet**

   ```bash
   git clone https://github.com/NathanAmoussou/M1S1_Sudoku
   ```

2. **Accéder au Répertoire du Projet**

   ```bash
   cd sudoku-solver
   ```

   *Remplacez `sudoku-solver` par le nom du répertoire si différent.*

## Exécution du Programme

Le programme principal est contenu dans le fichier `main.py`. Vous pouvez l'exécuter en utilisant la commande suivante :

```bash
python3 main.py
```

## Utilisation

### Entrer une Grille

Lors de l'exécution, le programme vous demandera d'entrer les 81 nombres de la grille de Sudoku, en utilisant `-1` pour représenter les cellules vides.
Il est également possible de passer une grille (contenu dans un fichier) en argument lors de l'appel de `main.py` dans le terminal.

**Exemple d'entrée :**

```
Entrer les 81 nombres de la grille de Sudoku (-1 pour les cellules vides), séparés par des espaces :
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 2 -1 3 -1 -1 -1 -1 -1 -1 3 -1 2 -1 -1 -1 1 -1 4 -1 -1 -1 -1 -1 -1 5 -1 -1 -1 -1 6 -1 -1 3 -1 -1 -1 -1 -1 -1 4 -1 7 -1 -1 8 -1 -1 -1 9 6 2 -1 -1 -1 7 -1 -1 -1
```
**Exemple d'entrée avec fichier :**

```
python3 main.py Other/input_test.txt
```
**Remarques :**

- Les nombres doivent être séparés par des espaces.
- Utilisez des nombres entre `1` et `9` pour les cellules remplies.
- Utilisez `-1` pour les cellules vides.

### Résolution de la Grille

Après avoir entré la grille, le programme affichera la grille parsée et tentera de la résoudre en appliquant les règles de déduction implémentées.

**Exemple d'affichage :**

```
Grille Sudoku parsée :
. . . | . . . | . . .
. . . | . . . | . . 1
. . . | . . 2 | . 3 .
---------------------
. . . | . . 3 | . 2 .
. . 1 | . 4 . | . . .
. . 5 | . . . | . 6 .
---------------------
. 3 . | . . . | . . 4
. 7 . | . 8 . | . . 9
6 2 . | . . 7 | . . .
```

### Interaction Utilisateur

Si le solveur ne parvient pas à résoudre la grille avec les règles de déduction disponibles, il vous proposera d'entrer manuellement une valeur pour une cellule spécifique.

**Exemple :**

```
Résolution impossible avec les règles de déduction implémentées.
Entrer une valeur pour la cellule (3, 3) parmi les candidats {6, 7} :
Votre entrée :
```

**Instructions :**

- Saisissez un nombre parmi les candidats proposés.
- Le programme tentera à nouveau de résoudre la grille avec cette nouvelle information.
- Ce processus peut se répéter si nécessaire.

## Fonctionnalités

- **Résolution Automatique** : Utilise des règles de déduction avancées pour résoudre la grille sans intervention de l'utilisateur si possible.
- **Évaluation de la Difficulté** : Affiche le niveau de difficulté de la grille (`Facile`, `Moyen`, `Difficile`, `Très difficile`, `Impossible`) en fonction des règles utilisées.
- **Interaction Utilisateur** : Permet à l'utilisateur d'entrer des valeurs lorsque le solveur ne peut pas progresser seul.
- **Affichage Clair** : Montre la grille de manière lisible avec des séparateurs pour les blocs de Sudoku.

## Exemples

### Résolution Réussie

```
Sudoku correctement résolu !
Grille de Sudoku actuelle:
[Affichage de la grille résolue]
Niveau de difficulté : Difficile
```

### Résolution avec Intervention de l'Utilisateur

```
Résolution impossible avec les règles de déduction implémentées.
Entrer une valeur pour la cellule (3, 3) parmi les candidats {6, 7} :
Votre entrée : 7
Sudoku correctement résolu après l'input !
Grille de Sudoku actuelle:
[Affichage de la grille résolue]
Niveau de difficulté : Très difficile
```

### Échec de Résolution

```
Résolution impossible même après l'input utilisateur.
La difficulté est probablement Impossible ou l'input était faux.
```

## Dépannage

- **Erreur : "Toutes les entrées doivent être des entiers entre -1 et 9."**
  - Assurez-vous que vous n'avez entré que des nombres entiers entre `-1` et `9`, sans caractères spéciaux ou lettres.
- **Le programme ne progresse pas après l'entrée de l'utilisateur.**
  - Vérifiez que vous avez entré une valeur valide parmi les candidats proposés.
  - Il se peut que la grille soit insolvable avec les règles implémentées.
- **Problèmes d'exécution du script.**
  - Assurez-vous que vous exécutez le script avec Python 3 (`python3 main.py`).
  - Vérifiez que tous les fichiers du projet sont présents dans le même répertoire.

## Conclusion

Ce solveur de Sudoku est un outil puissant pour résoudre et analyser des grilles de différentes difficultés. En suivant ce guide, vous devriez être en mesure d'utiliser le programme efficacement. N'hésitez pas à explorer les fonctionnalités avancées et à tester différentes grilles pour voir comment le solveur réagit.

**Bon Sudoku !**

---

**Contact :**

Pour toute question ou suggestion, veuillez contacter l'équipe de développement à [votre-email@example.com](mailto:votre-email@example.com).
