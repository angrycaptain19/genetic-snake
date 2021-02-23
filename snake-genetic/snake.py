import pygame
import os
import random
import numpy as np
import colors
import settings
import genetic_alg


DIRECTIONS = np.array([
(0, -1),  # UP
(1, 0),  # RIGHT
(0, 1),  # DOWN
(-1, 0)  # LEFT
])


class Snake():

	# random.seed(settings.seed)
	snake = None

	def __init__(self, individual, visual=True, replay=False, food_list = []):
		self.individual = individual
		if (visual == True):
			self.s = pygame.display.set_mode((settings.width, settings.height))
			self.score = 0

		# Starting position (random or not)
		if settings.start == "fixed":
			self.snake = np.array([[15, 26]])
			# self.snake = np.array([[15, 26], [15, 27], [15, 28], [15, 29]])
		elif settings.start == "random":
			self.snake = np.array([[random.randint(
				0, settings.display_size-1), random.randint(0, settings.display_size-1)]])
		# First Direction
		self.direction = 0  # UP

		self.food = []

		# First food placed
		if replay == False:
			self.generate_food()
		else :
			self.fruit = food_list[0]

		self.time_alive = 0
		self.last_fruit_time = 0

		# Variables to compute fitness
		self.fitness = 0.
		self.last_dist = np.inf
		self.death_type = 0

	def generate_food(self):
		self.fruit = [random.randint(
					0, settings.display_size-1), random.randint(1, settings.display_size-1)]
		self.food.append(self.fruit)

	def isfoodeaten(self):
		if all(self.snake[0] == self.fruit):
			# self.fruit = [random.randint(0, settings.display_size-1), random.randint(1, settings.display_size-1)]
			self.generate_food()
			self.score += 1
			self.last_fruit_time = 0
			return True
		else:
			# tail = self.snake[-1]
			self.snake = self.snake[:-1, :]

	def isdead1(self):
		if(self.snake[0][0] < 0 or
		self.snake[0][0] >= settings.display_size or
		self.snake[0][1] < 0 or
		self.snake[0][1] >= settings.display_size
		):
			self.death_type = 10
			return True
		elif(self.snake[0] in self.snake[10:]):
			self.death_type = 50
			return True


	# def isdead2(self):


	def calculate_fitness(self):
		# Fitness function
		self.fitness = self.time_alive + self.score**2 -self.last_fruit_time*self.death_type*2
		return self.fitness



		# print(inputs)

		# if outputs == 0:  # No change from current direction
		# 	pass
		# elif outputs == 1:  # Left from current direction
		# 	self.direction = (self.direction + 3) % 4
		# elif outputs == 2:  # Right from current direction
		# 	self.direction = (self.direction + 1) % 4

	def step(self, direction):
		old_head = self.snake[0]
		movement = DIRECTIONS[direction]
		new_head = old_head + movement

		if (
			new_head[0] < 0 or
			new_head[0] >= settings.display_size or
			new_head[1] < 0 or
			new_head[1] >= settings.display_size or
			new_head.tolist() in self.snake.tolist()
			):

			return False
		

		# if all(self.snake[0] == self.fruit):
		# 	# self.fruit = [random.randint(0, settings.display_size-1), random.randint(1, settings.display_size-1)]
		# 	self.generate_food()
		# 	self.score += 1
		# 	self.last_fruit_time = 0

		# else:

		# 	self.snake = self.snake[:-1, :]

		self.snake = np.concatenate([[new_head], self.snake], axis=0)
		return True

	def get_inputs(self):
		head = self.snake[0]
		inputs = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

		# check forward, left, right
		possible_dirs = [
			DIRECTIONS[self.direction],  # straight forward
			DIRECTIONS[(self.direction + 3) % 4],  # left
			DIRECTIONS[(self.direction + 1) % 4]  # right
		]

		for i, p_dir in enumerate(possible_dirs):
		# sensor range = 5
			for j in range(5):
				guess_head = head + p_dir * (j + 1)

				if (
					guess_head[0] < 0 or
					guess_head[0] >= settings.display_size or
					guess_head[1] < 0 or
					guess_head[1] >= settings.display_size or
					guess_head.tolist() in self.snake.tolist()
					):
					inputs[i] = j * 0.2
					break


		if settings.distance_type == "value":
			inputs[0] = 1 / abs(np.array(head[0])-settings.display_size)
			# West wall
			inputs[1] = 1 / abs(np.array(head[0])-0)
			# North wall
			inputs[2] = 1 / abs(np.array(head[1])-0)
			# South wall
			inputs[3] = 1 / abs(np.array(head[1])-settings.display_size)

		elif settings.distance_type == "binary":
			if abs(np.array(head[0])-settings.display_size) <= 2*settings.block_size:
				inputs[3] = 1
			elif abs(np.array(head[0])-0) <= 2*settings.block_size:
				inputs[4] = 1
			elif abs(np.array(head[1])-0) <= 2*settings.block_size:
				inputs[5] = 1
			elif abs(np.array(head[1])-settings.display_size) <= 2*settings.block_size:
				inputs[6] = 1


		if np.any(head == self.fruit) and np.sum(head * possible_dirs[0]) <= np.sum(self.fruit * possible_dirs[0]):
			inputs[7] = 1

		if np.sum(head * possible_dirs[1]) < np.sum(self.fruit * possible_dirs[1]):
			inputs[8] = 1
		else:
			inputs[9] = 1

		# for i in range(1, 4):
			
		# 	test = head + (possible_dirs[0] * i)
		# 	if (
		# 		np.any(test) < 0 or
		# 		np.any(test) >= settings.display_size or
		# 		np.any(test) > 0 or
		# 		np.any(test) <= settings.display_size or
		# 		test.tolist() in self.snake.tolist()
		# 		):
		# 		inputs[7] = 1

		# 	test = head + (possible_dirs[1] * i)
		# 	if (
		# 		np.any(test) < 0 or
		# 		np.any(test) >= settings.display_size or
		# 		np.any(test) > 0 or
		# 		np.any(test) <= settings.display_size or
		# 		test.tolist() in self.snake.tolist()
		# 		):
		# 		inputs[8] = 1

		# 	test = head + (possible_dirs[2] * i)
		# 	if (
		# 		np.any(test) < 0 or
		# 		np.any(test) >= settings.display_size or
		# 		np.any(test) > 0 or
		# 		np.any(test) <= settings.display_size or
		# 		test.tolist() in self.snake.tolist()
		# 		):
		# 		inputs[9] = 1

		return np.array(inputs)


	def run(self,visual=True, replay=False, food_list = []):
		# self.fitness = 0

		font = pygame.font.SysFont('arial', 12)
		fontbold = pygame.font.SysFont('arial', 15, bold=True)
		font.set_bold(True)

		clock = pygame.time.Clock()

		while True:
			clock.tick(settings.fps)

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
				if event.type == pygame.QUIT:
					exit() 

			# Convert output of NN to a direction for the snake to take
			if __name__ != '__main__':
				inputs = self.get_inputs()
				outputs = self.individual.forward(inputs)
				outputs = np.argmax(outputs)
				# print(inputs)
				# print(outputs)
				if outputs == 0: # No change from current direction
					self.direction = 0
				elif outputs == 1: # Left from current direction
					self.direction = (self.direction + 3) % 4
				elif outputs == 2: # Right from current direction
					self.direction = (self.direction + 1) % 4

				if not self.step(self.direction):
					break

				if self.isdead1():
					break

				# if self.isdead2():
				# 	break

				self.time_alive += 0.1
				self.last_fruit_time += 0.1

				# if replay==False:
				# 	self.isfoodeaten()
				# else:
				# 	food_list[0]

				self.isfoodeaten()

				self.calculate_fitness()

				# print(self.snake)

				# Kill Individual if it is looping

				if self.last_fruit_time > 10 :
					# print('Killed to avoid loop')
					self.death_type = 50
					break


				if (visual == True):
					# Display Background
					self.s.fill(colors.Pback)
					# Display Snake
					for body_part in self.snake:
						pygame.draw.rect(self.s, colors.Psnake, pygame.Rect(body_part[0] * settings.block_size, body_part[1] * settings.block_size, settings.block_size, settings.block_size), 2)
					# Display food
					pygame.draw.rect(self.s, colors.Pfood, pygame.Rect(self.fruit[0] * settings.block_size, self.fruit[1] * settings.block_size, settings.block_size, settings.block_size), 2)


				# Text on screen
				# Score
				Title1 = fontbold.render("Snake Stats : ", False, colors.grey)
				self.s.blit(Title1, (15, 0))

				CurrentScore = font.render("Score : " + str(self.score), False, colors.grey)
				self.s.blit(CurrentScore, (15, 15))

				CurrentFitness = font.render("Fitness : " + str(round(self.fitness, 2)), False, colors.grey)
				self.s.blit(CurrentFitness, (15, 30))

				TimeAlive = font.render("Time Alive : " + str(round(self.time_alive, 2)), False, colors.grey)
				self.s.blit(TimeAlive, (15, 45))

				LastFruit = font.render("Time since last fruit : " + str(round(self.last_fruit_time, 2)), False, colors.grey)
				self.s.blit(LastFruit, (15, 60))



				pygame.draw.rect(self.s, colors.grey, pygame.Rect(12, 0, 157, 75), 2)



				Title2 = fontbold.render("Settings : ", False, colors.grey)
				self.s.blit(Title2, (15, 80))

				SelectionSett = font.render("Selection : " + str(settings.selection_type), False, colors.grey)
				self.s.blit(SelectionSett, (15, 95))

				SelectionSett = font.render("Crossover : " + str(settings.crossover_type), False, colors.grey)
				self.s.blit(SelectionSett, (15, 110))

				SelectionSett = font.render("# Parents : " + str(settings.Nb_parents), False, colors.grey)
				self.s.blit(SelectionSett, (15, 125))

				pygame.draw.rect(self.s, colors.grey, pygame.Rect(12, 80, 160, 60), 2)

				pygame.display.update()

		return self.fitness, self.score, self.food
