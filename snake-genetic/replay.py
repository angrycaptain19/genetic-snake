import pickle 
import numpy as np
from snake import Snake

# Ajustement manuel pour identifier un individu spécifique dans une génération spécifique.
def replay(individuals_list, food_list, index):

    # individuals_list and food_list must be strings
    f = open(individuals_list, 'rb')
    individuals_list = pickle.load(f)
    f.close()

    f = open(food_list, 'rb')
    food_list = pickle.load(f)
    f.close()
    # index = individual-1
    individual = individuals_list[index][0]
    food = food_list[index]

    if __name__ != '__main__':
        print("-----------------------------")
        snake = Snake(individual=individual, visual=True, replay=True, food_list = food)
        fitness, score, food = snake.run(visual=True, food_list = food)
        
        print(food_list)
        
        print(fitness)
        
