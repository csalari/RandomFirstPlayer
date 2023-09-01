import random

# Create an empty list to store player names
players = []

# Get the number of players from the user
num_players = int(input("Enter the number of players: "))

# Get player names from the user and add them to the list
for i in range(num_players):
    player_name = input(f"Enter the name of player {i + 1}: ")
    players.append(player_name)

# Randomly select an initial player
initial_player = random.choice(players)

# Print the selected initial player
print("The initial player is:", initial_player)
