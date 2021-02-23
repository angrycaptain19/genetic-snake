
seed = 30

fps = 60
display_size = 30
block_size = 20

width = display_size * block_size
height = display_size * block_size

# global settings
pop = 25
generations = 100

# genetic population settings
# top best parents
Nb_top_best = 5

# Tournament
Nb_top_tourn_drawn = 20
Nb_top_tourn_kept = 2

#random
Nb_top_rand = pop/2

Nb_children = 2 # Max 10
Proba_Muta = 0.4

# Valid choices are "tournament" / "best_parents" / "random"
selection_type = "best_parents"

# Valid choices are "value" / "binary"
distance_type = "binary"

# Valid choices are "fixed" / "random"
start = "fixed"

# Valid choices are "bi-parent" / "multi-parent"
crossover_type = "bi-parent"
# If multi-parent approach (has to be even for now):
Nb_parents = 4

if crossover_type == "bi-parent":
    Nb_parents = 2
else:
    pass