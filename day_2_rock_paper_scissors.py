from example_inputs.day_2 import example_input
from real_inputs.day_2 import real_input

def calculate_selection_score(selection: str) -> int:
    selection_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return selection_score[selection]

def calculate_score_single_game_v2(line: str) -> int:
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win
    they_played = line[0]
    you_win_or_lose = line[2]
    game_score = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    your_score = game_score[you_win_or_lose]
    your_selection = {
        "A": {
            "X": "Z",
            "Y": "X",
            "Z": "Y",
        },
        "B": {
            "X": "X",
            "Y": "Y",
            "Z": "Z",
        },
        "C": {
            "X": "Y",
            "Y": "Z",
            "Z": "X",
        }
    }
    your_score = your_score + calculate_selection_score(your_selection[they_played][you_win_or_lose])
    return your_score

def calculate_need_to_win(games_played: str):
    games_played_list = games_played.split("\n")
    total_score = 0
    for game in games_played_list:
        total_score = total_score + calculate_score_single_game_v2(game)
    return total_score


def calculate_score_single_game(line: str) -> int:
    they_played = line[0]
    you_played = line[2]
    your_score = calculate_selection_score(you_played)
    game_score = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        }
    }
    your_score = your_score + game_score[they_played][you_played]

    # They selected
    # A for Rock
    # B for Paper
    # C for Scissors

    # You selected
    # X for Rock 1
    # Y for Paper 2
    # Z for Scissors 3
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

    # shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    return your_score

def calculate_score_all_games(games_played: str):
    games_played_list = games_played.split("\n")
    total_score = 0
    for game in games_played_list:
        total_score = total_score + calculate_score_single_game(game)
    return total_score






print(calculate_score_all_games(example_input))
print(calculate_score_all_games(real_input))
print(calculate_need_to_win(example_input))
print(calculate_need_to_win(real_input))
