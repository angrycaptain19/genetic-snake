# genetic-snake
Utiliser un réseau de neurone (FeedForward) pour permettre un apprentissage machine à l’aide d’un algorithme génétique, en utilisant différents scénarios afin de comparer le résultat final des différents modèles.

Le réseau de neurone effectuera son apprentissage pour chaque individu en ajustant ses poids selon les poids de ses “parents”, jusqu’à atteindre la meilleure performance possible au bout d’un certain nombre de générations.

# Utilisation du code


```
$ run main.py
```
L'apprentissage de l'agent est automatiquement sauvegardé dans des fichiers pickle, nommés par défaut *food-list.pkl* (qui stockera la séquence de nourriture dont la génération est initialement aléatoire) et *individuals-list.pkl* (qui stockera les mouvements du serpent). Il est possible de rejouer ces informations de cette façon:

```
$ run replay.py "food-list.pkl" "individuals-list.pkl"
```
