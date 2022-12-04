with open('input/input02.txt') as f:
    lines = [i.strip() for i in f.readlines()]


# part one
def get_shape_points(choice):
    if choice == 'A':
        return 1
    elif choice == 'B':
        return 2
    elif choice == 'C':
        return 3


def map_user_choice(user_choice):
    if user_choice == 'X':
        return 'A'
    elif user_choice == 'Y':
        return 'B'
    elif user_choice == 'Z':
        return 'C'


def get_round_outcome(opponent_choice, user_choice):
    mapped_user_choice = map_user_choice(user_choice)

    if (opponent_choice == mapped_user_choice):
        return 'DRAW'
    elif (opponent_choice == 'A' and mapped_user_choice == 'B'):
        return 'WIN'
    elif (opponent_choice == 'A' and mapped_user_choice == 'C'):
        return 'LOSE'
    elif (opponent_choice == 'B' and mapped_user_choice == 'A'):
        return 'LOSE'
    elif (opponent_choice == 'B' and mapped_user_choice == 'C'):
        return 'WIN'
    elif (opponent_choice == 'C' and mapped_user_choice == 'A'):
        return 'WIN'
    elif (opponent_choice == 'C' and mapped_user_choice == 'B'):
        return 'LOSE'


def get_outcome_points(outcome):
    if outcome == 'WIN':
        return 6
    elif outcome == 'DRAW':
        return 3
    elif outcome == 'LOSE':
        return 0


def get_round_points(opponent_choice, user_choice):
    shape_points = get_shape_points(map_user_choice(user_choice))
    outcome_points = get_outcome_points(get_round_outcome(opponent_choice, user_choice))
    return shape_points + outcome_points


def perform_round(game_line):
    opponent_choice = game_line[0]
    user_choice = game_line[2]
    return get_round_points(opponent_choice, user_choice)


total_points = 0
for game_line in lines:
    total_points += perform_round(game_line)

print('Answer 1: ', total_points)


def map_user_choice_to_outcome(user_choice):
    if user_choice == 'X':
        return 'LOSE'
    elif user_choice == 'Y':
        return 'DRAW'
    elif user_choice == 'Z':
        return 'WIN'


def get_round_choice(opponent_choice, outcome):
    if (outcome == 'DRAW'):
        return opponent_choice
    elif (outcome == 'WIN' and opponent_choice == 'A'):
        return 'B'
    elif (outcome == 'WIN' and opponent_choice == 'B'):
        return 'C'
    elif (outcome == 'WIN' and opponent_choice == 'C'):
        return 'A'
    elif (outcome == 'LOSE' and opponent_choice == 'A'):
        return 'C'
    elif (outcome == 'LOSE' and opponent_choice == 'B'):
        return 'A'
    elif (outcome == 'LOSE' and opponent_choice == 'C'):
        return 'B'


def perform_round_two(game_line):
    opponent_choice = game_line[0]
    desired_outcome = game_line[2]

    outcome = map_user_choice_to_outcome(desired_outcome)
    user_choice = get_round_choice(opponent_choice, outcome)
    shape_points = get_shape_points(user_choice)

    outcome_points = get_outcome_points(outcome)
    return shape_points + outcome_points


total_points = 0
for game_line in lines:
    total_points += perform_round_two(game_line)

print('Answer 2: ', total_points)
