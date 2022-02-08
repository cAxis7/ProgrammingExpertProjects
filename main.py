import team_functions as tf

num_teams = tf.get_number_of_teams()
team_names = tf.get_team_names(num_teams)
games_played = tf.get_number_of_games_played(num_teams)
team_wins = tf.get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_wins, key=lambda item: item[1])
game_pairings = []

games_to_make = len(sorted_teams)//2

for game_num in range(games_to_make):
  home_team = sorted_teams[game_num][0]
  away_team = sorted_teams[num_teams - 1 - game_num][0]
  game_pairings.append([home_team, away_team])

for pairing in game_pairings:
  home_team, away_team = pairing
  print(f"Home: {home_team} VS Away: {away_team}")

