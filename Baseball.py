import os
import sys


def teams_read(folder_name):
    teams_data_tuple = []
    teams_file_path = os.path.join(folder_name, "teams.dat")
    with open(teams_file_path, "r") as f:
        teams_data = f.read().splitlines()
    f.close()
    for teams in teams_data:
        split_teams = teams.split(":")
        team_name = split_teams[0]
        team_code = split_teams[1]
        teams_tuple = (team_code, team_name)
        teams_data_tuple.append(teams_tuple)
    return teams_data_tuple


def games_read(folder_name):
    games_tuple_list = []
    games_file_path = os.path.join(folder_name, "games.dat")
    with open(games_file_path, "r") as f:
        games_data = f.read().splitlines()
    f.close()
    for game in games_data:
        split_games = game.split(":")
        game_date = split_games[0]
        team_code_home = split_games[1]
        team_code_away = split_games[2]
        game_home_score = int(split_games[3])
        game_away_score = int(split_games[4])
        games_tuple = (game_date, team_code_home, team_code_away, game_home_score, game_away_score)
        games_tuple_list.append(games_tuple)

    return games_tuple_list


def calculate_team_standings(teams_data, games_data):
    standings = []
    teams_standing = {}
    for game in games_data:
        game_date, team_code_1, team_code_2, game_score_1, game_score_2 = game
        if game_score_1 > game_score_2:
            wins = team_code_1
            loses = team_code_2
        elif game_score_2 > game_score_1:
            wins = team_code_2
            loses = team_code_1
        else:
            wins = loses = "TIE"

        for team in [team_code_1, team_code_2]:
            if team not in teams_standing:
                teams_standing[team] = {"WIN": 0, "LOSS": 0, "TIE": 0}
        for team in [team_code_1, team_code_2]:
            if team == wins:
                teams_standing[team]["WIN"] += 1
            elif team == loses:
                teams_standing[team]["LOSS"] += 1
            else:
                teams_standing[team]["TIE"] += 1
    for team_code, team_name in teams_data:
        total_games = teams_standing[team_code]["WIN"] + teams_standing[team_code]["LOSS"] + teams_standing[team_code][
            "TIE"]
        team_wins = teams_standing[team_code]["WIN"]
        team_losses = teams_standing[team_code]["LOSS"]
        team_ties = teams_standing[team_code]["TIE"]
        team_percent = (team_wins + 0.5 * team_ties) / total_games
        team_percent_rounded = round(team_percent, 3)
        standings.append((team_code, team_wins, team_losses, team_ties, team_percent_rounded))
        standings_sorted = sorted(standings, key=lambda x: x[4], reverse=True)
    print("TEAM                   WINS LOSSES   TIES PERCENT")
    print("-------------------- ------ ------ ------ -------")
    for i in standings_sorted:
        print(f"{i[0]:<20s}{i[1]:>7d}{i[2]:>7d}{i[3]:>7d}{i[4]:^10.3f}")
    return standings_sorted


def calculate_team_results(teams_data, games_data):
    teams_wins = 0
    teams_loss = 0
    teams_ties = 0
    found = True
    while found:
        team_input_code = input("Enter team code (e.g. ARI, ATL, CHC, CLE, STL): ").strip().upper()
        for team in teams_data:
            team_code, team_name = team[0], team[1]
            if team_input_code == team_code:
                print(f"Team: {team_name}")
                print("      DATE   OPPONENT        US  THEM  RESULT")
                found = False
                for game in games_data:
                    date, code1, code2, score1, score2 = game[0], game[1], game[2], int(game[3]), int(game[4])
                    if code1 == team_code:
                        if score1 > score2:
                            result = "WIN"
                        elif score1 == score2:
                            result = "TIE"
                        else:
                            result = "LOSS"
                        print(f"{date:<14s}    {code2:<11s}{score1:>2d}{score2:>6d}{result:>8s}")
                        if result == "WIN":
                            teams_wins += 1
                        elif result == "LOSS":
                            teams_loss += 1
                        else:
                            teams_ties += 1

                    elif code2 == team_code:
                        if score2 > score1:
                            result = "WIN"
                        elif score1 == score2:
                            result = "TIE"
                        else:
                            result = "LOSS"
                        print(f"{date:<14s} at {code1:<11s}{score2:>2d}{score1:>6d}{result:>8s}")

                        if result == "WIN":
                            teams_wins += 1
                        elif result == "LOSS":
                            teams_loss += 1
                        else:
                            teams_ties += 1
                print(f"Overall Record: {teams_wins}-{teams_loss}-{teams_ties}")

                break
        else:
            print("Invalid team code. Please enter a valid code name.")


def quit_program():
    exit()


def main():
    folder = sys.argv[1:]
    folder_name = folder[0].lower()
    teams_data = teams_read(folder_name)
    games_data = games_read(folder_name)
    while True:
        input_choice = input("What do you want to see? \n(s) Standings\n(t) Team results\n(q) Quit\n ").strip().lower()
        if input_choice == 's':
            calculate_team_standings(teams_data, games_data)
        elif input_choice == 't':
            calculate_team_results(teams_data, games_data)
        elif input_choice == 'q':
            quit_program()
        else:
            print("Invalid input, only input: s, t , q")


main()
