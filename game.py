import copy
import datetime
import json
import random
import time

POSSIBLE_ANSWERS = {0: 'a.', 1: 'b.', 2: 'c.', 3: 'd.'}


def change_highscore(player_id: str, score: int, path: str = "users.json"):
    try:
        with open(path, "r+") as f:
            players = json.loads(f.read())
            players[player_id]['high_score'] = score
            players[player_id]['date'] = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M")
            f.seek(0)
            f.write(json.dumps(players, indent=4))
    except Exception as e:
        print(f"Failed to save the high score of {player_id}.\n Error is {e}.")
    else:
        print("Successfully saved the new high score.")


def run_game(player: dict, questions_path: str = "questions.json") -> int:
    score = 0
    with open(questions_path, "r") as f:
        questions = json.loads(f.read())
        questions = questions['questions']

    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        question_object = random.choice(copy_questions)

        # print(question_object)
        print(question_object['question'])
        for index, answer in enumerate(question_object['answers']):
            print(f"{POSSIBLE_ANSWERS[index]} {answer}")

        pick = input("Pick the right answer: ")
        answers = {v: k for k, v in POSSIBLE_ANSWERS.items()}
        if answers[f"{pick}."] == question_object['correctIndex']:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")

        copy_questions.remove(question_object)
        time.sleep(1)

    print(f"You have answered to {score} questions correctly!")

    if score > player[list(player.keys())[0]]['high_score']:
        change_highscore(player_id=list(player.keys())[0], score= score)

    return 1