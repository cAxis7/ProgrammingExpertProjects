def get_number_of_teams():
  while True:
    num_teams = int(input("Enter the number of teams in the tournament: "))

    if num_teams > 1:
      break
    
    print("The minimum number of teams is 2, try again.")
  
  return num_teams

def get_team_names(num_teams):
  team_names = []

  for i in range(num_teams):
    while True:
      team_name = input(f"Enter the name for team #{i + 1}: ")
      num_words = len(team_name.split(" "))

      if num_words > 2:
        print("Team names may have at most 2 words, try again.")
      elif len(team_name) < 2:
        print("Team names must have at least 2 characters, try again.")
      else:
        break
  
    team_names.append(team_name)

  return team_names

def get_number_of_games_played(num_teams):
  while True:
    games_played = int((input("Enter the number of games played by each team: ")))

    if games_played >= num_teams - 1:
      break

    print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
  
  return games_played

def get_team_wins(team_names, games_played):
  team_wins = []

  for team in team_names:
    while True:
      wins = int(input(f"Enter the number of wins Team {team} had: "))

      if wins > games_played:
        print(
          f"The maximum number of wins is {games_played}, try again."
        )
      elif wins < 0:
        print("The minimum number of wins is 0, try again.")
      else:
        break
    
    team_wins.append((team, wins))

  return team_wins
