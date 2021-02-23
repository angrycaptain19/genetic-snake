# genetic-snake
Utiliser un réseau de neurone (FeedForward) pour permettre un apprentissage machine à l’aide d’un algorithme génétique, en utilisant différents scénarios afin de comparer le résultat final des différents modèles.

Le réseau de neurone effectuera son apprentissage pour chaque individu en ajustant ses poids selon les poids de ses “parents”, jusqu’à atteindre la meilleure performance possible au bout d’un certain nombre de générations.
Le réseau de neurone pour un individu donné aura comme input une vision en quatre ou huit directions cardinales placée à la tête du serpent, qui lui donnera les informations suivantes :

• La distance entre la tête du serpent et la nourriture, si elle existe pour une direction donnée, sinon ce sera un 0. (Possibilité d’utiliser une variable binaire si oui ou non voit au lieu de distance)

• La distance entre la tête du serpent et le mur, si elle existe pour une direction donnée, sinon ce sera un 0. (Possibilité d’utiliser une variable binaire si oui ou non voit au lieu de distance)

• La distance entre la tête du serpent et son corps, si elle existe pour une direction donnée, sinon ce sera un 0. (Possibilité d’utiliser une variable binaire si oui ou non voit au lieu de distance)

L’output sera la direction que le serpent devrait prendre (4 neurones).

Les différents modèles à comparer vont varier en fonction de la méthode de sélection des individus pour la repopulation :

• Une approche “Multi-parent recombination”(Link) Vs “Two parents recombination” pour la recombinaison des “chromosomes” (poids) pour la génération suivante.

• La stratégie pour le choix de la génération suivante :

o Ne garder que les deux (ou multi-parents) meilleurs candidats de la génération pour re-populer entièrement la génération suivante.
o Utiliser l’approche “Tournament selection”(Link) pour sélectionner une population de parents.
o Choix au hasard pour une population de comparaison
