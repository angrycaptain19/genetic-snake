import pygame, random
import numpy as np
from copy import deepcopy
from snake import Snake
from NN import NN
import settings
import pickle 

'''
This finds the best 2 individuals in a given generation which are used to generate the next generation
'''

def gen_alg():
    #s = pygame.display.set_mode((settings.width, settings.height))
    
   # generate 1st population
    # random.seed(settings.seed)
    individuals = [NN() for _ in range(settings.pop)]
    best_fitness = -100
    fitness_list = []
    food_list = []
    best_individuals = []
    nnobject = []
    listtest = []
    next_gen = []

    n_gen = 0
    while n_gen < settings.generations :
        n_gen += 1

        # Done for every individual in current gen
        for i, individual in enumerate(individuals):
            snake = Snake(individual=individual, visual=True)
            fitness, score, food = snake.run(visual=True)
            
            nnobject.append(individual)
            
            fitness_list.append(fitness)
            
            food_list.append(food)

            listtest.append([individual, fitness])
            
            if fitness > best_fitness:
                # print(fitness_list)
                best_fitness = fitness
                best_individal = i+1
            
            # print('Gen %s, Individual %s/%s : Fitness: %s, Score: %s' % (n_gen, i+1, settings.pop, fitness, score))
            # print(score)
            
        # Done for every gen
        print('****** Gen #%s  ////  Best Fit attained %s ///  By individual %s ******' % (n_gen, round(best_fitness, 2), best_individal))
        

        # Save for replay
        f = open('individuals-list.pkl', 'wb')
        pickle.dump(listtest, f)
        f.close()
        
        f = open('food-list.pkl', 'wb')
        pickle.dump(food_list, f)
        f.close()

        ### Selection ###

        if settings.selection_type == "best_parents":
            ### Best parents ###
            # best_individuals = deepcopy(sorted_individuals[:settings.Nb_top_best])
            # print("bef "+ str(listtest))
            listtest.sort(key=lambda x: x[1], reverse=True)
            # print("aft "+ str(listtest))
            best_individuals = deepcopy(listtest[:settings.Nb_top_best])
            # print("best " + str(best_individuals))

        elif settings.selection_type == "tournament":
            ### Tournament Selection ###
            # best_individuals
            for i in range(0, settings.Nb_top_tourn_kept):
                tournament = []
                for j in range(0, settings.Nb_top_tourn_drawn):
                    tournament.append(random.choice(listtest))
                # print("bef "+ str(tournament))
                tournament.sort(key=lambda x: x[1], reverse=True)
                # print("aft "+ str(tournament))
                best_individuals.append(tournament[0])
        
        elif settings.selection_type == "random":
            ### Random choice ###
            for i in range(0, int(settings.Nb_top_rand)):
                best_individuals.append(random.choice(listtest))

        ### Crossover ###
        if settings.crossover_type == "bi-parent":
        ### Bi-parent Approach ###
            for i in range(settings.pop):
                new_individual = deepcopy(best_individuals[0][0]) ## Added [0][0]
                a_individual = deepcopy(best_individuals[0][0])
                b_individual = deepcopy(best_individuals[1][0])

                cut = random.randint(0, new_individual.w1.shape[1])
                new_individual.w1[:, :cut] = a_individual.w1[:, :cut]
                new_individual.w1[:, cut:] = b_individual.w1[:, cut:]

                cut = random.randint(0, new_individual.w2.shape[1])
                new_individual.w2[:, :cut] = a_individual.w2[:, :cut]
                new_individual.w2[:, cut:] = b_individual.w2[:, cut:]

                cut = random.randint(0, new_individual.w3.shape[1])
                new_individual.w3[:, :cut] = a_individual.w3[:, :cut]
                new_individual.w3[:, cut:] = b_individual.w3[:, cut:]

                cut = random.randint(0, new_individual.w4.shape[1])
                new_individual.w4[:, :cut] = a_individual.w4[:, :cut]
                new_individual.w4[:, cut:] = b_individual.w4[:, cut:]

                next_gen.append(new_individual)

        ### Multi-parent Approach ###
        elif settings.crossover_type == "multi-parent":
            for i in range(settings.pop):
                new_individual = deepcopy(best_individuals[0][0]) ## Added [0][0]
                a_individual = deepcopy(best_individuals[0][0])
                b_individual = deepcopy(best_individuals[1][0])
                c_individual = deepcopy(best_individuals[2][0])
                d_individual = deepcopy(best_individuals[3][0])

                cut_1 = random.randint(0, new_individual.w1.shape[1])
                cut_2 = random.randint(cut_1, new_individual.w1.shape[1])
                cut_3 = random.randint(cut_2, new_individual.w1.shape[1])
                new_individual.w1[:, :cut_1] = a_individual.w1[:, :cut_1]
                new_individual.w1[:, cut_1:cut_2] = b_individual.w1[:, cut_1:cut_2]
                new_individual.w1[:, cut_2:cut_3] = c_individual.w1[:, cut_2:cut_3]
                new_individual.w1[:, cut_3:] = d_individual.w1[:, cut_3:]

                cut_1 = random.randint(0, new_individual.w2.shape[1])
                cut_2 = random.randint(cut_1, new_individual.w2.shape[1])
                cut_3 = random.randint(cut_2, new_individual.w2.shape[1])
                new_individual.w2[:, :cut_1] = a_individual.w2[:, :cut_1]
                new_individual.w2[:, cut_1:cut_2] = b_individual.w2[:, cut_1:cut_2]
                new_individual.w2[:, cut_2:cut_3] = c_individual.w2[:, cut_2:cut_3]
                new_individual.w2[:, cut_3:] = d_individual.w2[:, cut_3:]

                cut_1 = random.randint(0, new_individual.w3.shape[1])
                cut_2 = random.randint(cut_1, new_individual.w3.shape[1])
                cut_3 = random.randint(cut_2, new_individual.w3.shape[1])
                new_individual.w3[:, :cut_1] = a_individual.w3[:, :cut_1]
                new_individual.w3[:, cut_1:cut_2] = b_individual.w3[:, cut_1:cut_2]
                new_individual.w3[:, cut_2:cut_3] = c_individual.w3[:, cut_2:cut_3]
                new_individual.w3[:, cut_3:] = d_individual.w3[:, cut_3:]

                cut_1 = random.randint(0, new_individual.w4.shape[1])
                cut_2 = random.randint(cut_1, new_individual.w4.shape[1])
                cut_3 = random.randint(cut_2, new_individual.w4.shape[1])
                new_individual.w4[:, :cut_1] = a_individual.w4[:, :cut_1]
                new_individual.w4[:, cut_1:cut_2] = b_individual.w4[:, cut_1:cut_2]
                new_individual.w4[:, cut_2:cut_3] = c_individual.w4[:, cut_2:cut_3]
                new_individual.w4[:, cut_3:] = d_individual.w4[:, cut_3:]

                next_gen.append(new_individual)


        ### Mutation ### 
        # https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm) -> Gaussian
        individuals = []
        nn_w1 = []
        nn_w2 = []
        nn_w3 = []
        nn_w4 = []

        for i in range(len(nnobject)):
            nn_w1.append(nnobject[i].w1)
            nn_w2.append(nnobject[i].w2)
            nn_w3.append(nnobject[i].w3)
            nn_w4.append(nnobject[i].w4)


        w1_mean = np.mean(nn_w1)
        w2_mean = np.mean(nn_w2)
        w3_mean = np.mean(nn_w3)
        w4_mean = np.mean(nn_w4)

        w1_std = np.std(nn_w1) 
        w2_std = np.std(nn_w2)
        w3_std = np.std(nn_w3)
        w4_std = np.std(nn_w4)

        for i in range(int(settings.pop)):
            new_individual = deepcopy(next_gen[i])

            if random.uniform(0, 1) < settings.Proba_Muta:
                new_individual.w1 += new_individual.w1 * np.random.normal(w1_mean, w1_std, size=(10, 10)) / 100
            if random.uniform(0, 1) < settings.Proba_Muta:
                new_individual.w2 += new_individual.w2 * np.random.normal(w2_mean, w2_std, size=(10, 20)) / 100
            if random.uniform(0, 1) < settings.Proba_Muta:
                new_individual.w3 += new_individual.w3 * np.random.normal(w3_mean, w3_std, size=(20, 10)) / 100
            if random.uniform(0, 1) < settings.Proba_Muta:
                new_individual.w4 += new_individual.w4 * np.random.normal(w4_mean, w4_std, size=(10, 3)) / 100

            individuals.append(new_individual)


    
    return
