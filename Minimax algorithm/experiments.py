import numpy as np
import matplotlib.pyplot as plt
import math
import tic_tac_toe

labels = 'Win', 'Tie', 'Loss'
colors = ['green','grey','red']

def Grid_3x3(depth, rounds):
	
	fig, axs = plt.subplots(3, 3)
	fig.set_figheight(12)
	fig.set_figwidth(18)
	fig.suptitle(f"Experiment for tic tac toe AI with depth={depth} on 3X3 Grid", fontsize=16)

	for d in range (10):
		if (d == depth):
			continue

		wins = 0
		losses = 0
		draws = 0

		for i in range(rounds):
			grid = tic_tac_toe.generate_grid(3)
			winner = None
			if (i%2 == 0):
				winner = tic_tac_toe.play_game(grid, tic_tac_toe.GameMode.AI_vs_AI, 0, "X", d, depth, False)
			else:
				winner = tic_tac_toe.play_game(grid, tic_tac_toe.GameMode.AI_vs_AI, 0, "O", d, depth, False)

			if (winner == "O"):
				wins += 1
			elif (winner == "X"):
				losses += 1
			else:
				draws += 1

		values = [wins, draws, losses]
		if (d > depth):
			if (d % 3 == 0):
				axs[math.floor(d / 3) - 1, 2].set_title(f"d={depth} vs d={d}")
				patches, texts, autotexts = axs[math.floor(d / 3) - 1, 2].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)
			else:
				axs[math.floor(d / 3), (d % 3) - 1].set_title(f"d={depth} vs d={d}")
				patches, texts, autotexts = axs[math.floor(d / 3), (d % 3) - 1].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)
		else:
			axs[math.floor(d / 3), d % 3].set_title(f"d={depth} vs d={d}")
			patches, texts, autotexts = axs[math.floor(d / 3), d % 3].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)


		plt.setp(autotexts, size='x-small')
		for text in texts:
			text.set_color('white')
		for autotext in autotexts:
			autotext.set_color('black')

		plt.setp(autotexts, size=12)
	plt.legend()

	plt.show()



def Grid_4x4(depth, rounds):
	fig, axs = plt.subplots(2, 2)
	fig.set_figheight(12)
	fig.set_figwidth(18)
	plt.title(f"Experiment for tic tac toe AI with depth={depth} on 4X4 Grid", fontsize=16)
	for d in range (5):
		if (d == depth):
			continue

		wins = 0
		losses = 0
		draws = 0

		for i in range(rounds):
			grid = tic_tac_toe.generate_grid(4)
			winner = None
			if (i%2 == 0):
				winner = tic_tac_toe.play_game(grid, tic_tac_toe.GameMode.AI_vs_AI, 0, "X", d, depth, False)
			else:
				winner = tic_tac_toe.play_game(grid, tic_tac_toe.GameMode.AI_vs_AI, 0, "O", d, depth, False)

			if (winner == "O"):
				wins += 1
			elif (winner == "X"):
				losses += 1
			else:
				draws += 1

		values = [wins, draws, losses]
		if (d > depth):
			if (d % 2 == 0):
				axs[math.floor(d / 2) - 1, 1].set_title(f"d={depth} vs d={d}")
				patches, texts, autotexts = axs[math.floor(d / 2) - 1, 1].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)
			else:
				print(math.floor(d / 2), (d % 2) - 1, d)
				axs[math.floor(d / 2), (d % 2) - 1].set_title(f"d={depth} vs d={d}")
				patches, texts, autotexts = axs[math.floor(d / 2), (d % 2) - 1].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)
		else:
			axs[math.floor(d / 2), d % 2].set_title(f"d={depth} vs d={d}")
			patches, texts, autotexts = axs[math.floor(d / 2), d % 2].pie(values, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)


		plt.setp(autotexts, size='x-small')
		for text in texts:
			text.set_color('white')
		for autotext in autotexts:
			autotext.set_color('black')

		plt.setp(autotexts, size=12)


	plt.legend()

	plt.show()



if __name__ == "__main__":
	plt.style.use('dark_background')
	Grid_3x3(4, 50)
	#Grid_4x4(2, 100)