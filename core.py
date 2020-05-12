import matplotlib.pyplot as plt
import numpy as np

'''
    wins (5/10)
        Mark: 5
        Penny: 7
        Alex: 6
        Josh: 7
    
    data key (# = game number)
        #[0] = number of rolls
        #[1] = winner
        #[2..12] = roll count
'''

plot_roll = 0
plot_wins = 0
print_stats = 1

players = ["mark", "penny", "alex", "josh"]
roll_probability = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# data
one = np.array([47, 3, 0, 2, 3, 3, 11, 4, 8, 7, 6, 2, 1])
two = np.array([62, 2, 1, 4, 9, 7, 4, 12, 5, 5, 3, 7, 5])
three = np.array([58, 1, 1, 5, 5, 4, 6, 7, 10, 12, 4, 3, 1])
four = np.array([68, 1, 2, 0, 4, 4, 9, 13, 21, 6, 4, 4, 1])
five = np.array([57, 3, 1, 2, 5, 5, 8, 10, 7, 6, 8, 4, 1])
six = np.array([33, 2, 0, 5, 4, 1, 5, 5, 3, 5, 2, 2, 1])
seven = np.array([67, 2, 2, 2, 7, 7, 13, 12, 10, 6, 4, 2, 2])
eight = np.array([51, 1, 1, 1, 3, 7, 4, 5, 10, 6, 6, 5, 3])
nine = np.array([38, 2, 1, 6, 3, 1, 8, 2, 9, 3, 3, 1, 1])
ten = np.array([49, 2, 0, 3, 6, 6, 9, 4, 6, 8, 3, 3, 1])
eleven = np.array([58, 1, 2, 7, 1, 10, 8, 11, 8, 6, 4, 1, 0])
twelve = np.array([46, 1, 0, 2, 7, 6, 11, 4, 5, 6, 3, 1, 1])
thirteen = np.array([49, 3, 2, 6, 2, 4, 11, 8, 5, 4, 3, 3, 1])
fourteen = np.array([40, 0, 2, 2, 3, 5, 5, 5, 6, 5, 2, 2, 3])
fifteen = np.array([46, 0, 0, 3, 7, 3, 7, 10, 2, 6, 3, 4, 1])
sixteen = np.array([57, 3, 3, 4, 5, 6, 2, 12, 4, 4, 9, 4, 4])
seventeen = np.array([53, 3, 2, 3, 5, 6, 8, 9, 9, 5, 1, 4, 1])
eighteen = np.array([66, 0, 4, 4, 6, 10, 8, 9, 3, 5, 7, 5, 5])
nineteen = np.array([38, 1, 1, 2, 0, 9, 1, 4, 10, 9, 0, 2, 0])
twenty = np.array([65, 2, 1, 5, 2, 5, 15, 10, 6, 12, 2, 6, 1])
twentyone = np.array([67, 1, 2, 4, 5, 8, 10, 10, 7, 9, 6, 4, 2])
twentytwo = np.array([44, 3, 0, 1, 4, 8, 8, 5, 5, 5, 2, 3, 3])
twentythree = np.array([47, 3, 1, 8, 7, 7, 3, 5, 6, 4, 4, 2, 0])
twentyfour = np.array([41, 0, 2, 5, 4, 4, 8, 4, 7, 3, 2, 0, 2])
twentyfive = np.array([40, 0, 2, 4, 1, 5, 11, 5, 5, 4, 2, 1, 0])

total = np.array([one, two, three, four, five, six, seven, eight, nine, ten,
                  eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
                  twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive])

if print_stats:

    wins = np.array([0, 0, 0, 0])
    shortest = 999
    shortest_winner = ""
    longest = 0
    longest_winner = ""
    average_length = 0
    average_length_of_wins = np.array([0, 0, 0, 0])
    average_consistency_of_wins = np.array([0, 0, 0, 0])

    for game_index in range(0, total.__len__()):
        deviation = 0
        game_rolls = total[game_index][0]
        if game_rolls < shortest:
            shortest = game_rolls
            shortest_winner = players[total[game_index][1]]
        if game_rolls > longest:
            longest = game_rolls
            longest_winner = players[total[game_index][1]]
        average_length += game_rolls

        for roll_index in range(2, 13):
            deviation += abs(total[game_index][roll_index] - (game_rolls * roll_probability[roll_index - 2]))
        average_consistency_of_wins[total[game_index][1]] += deviation
        average_length_of_wins[total[game_index][1]] += game_rolls
        wins[total[game_index][1]] += 1

    for player_index in range(0, 4):
        average_consistency_of_wins[player_index] = average_consistency_of_wins[player_index] / wins[player_index]
        average_length_of_wins[player_index] = average_length_of_wins[player_index] / wins[player_index]

    average_length = average_length / total.__len__()

    print("average game length: {0} rolls".format(average_length))
    print("longest game: {0} won after {1} rolls".format(longest_winner, longest))
    print("shortest game: {0} won after {1} rolls".format(shortest_winner, shortest))
    print("average game length when players won...")
    for player_index in range(0, 4):
        print("  {0}: {1}".format(players[player_index], average_length_of_wins[player_index]))
    print("average roll consistency when player won...")
    for player_index in range(0, 4):
        print("  {0}: {1}".format(players[player_index], average_consistency_of_wins[player_index]))
    print("total wins...")
    for player_index in range(0, 4):
        print("  {0}: {1}".format(players[player_index], wins[player_index]))

'''
# get total rolls in a game
for game_index in range(0, total.__len__()):
    total_rolls = 0
    game = total[game_index]
    for roll_index in range(2, 13):
        total_rolls += game[roll_index]
    print("game {0}: {1}".format(game_index+1, total_rolls))
'''
