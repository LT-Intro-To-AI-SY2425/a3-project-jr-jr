from players import player_db
from match import match
from typing import List, Tuple, Callable, Any



def get_name(player: Tuple[str, int, List[str]]) -> str:
    return player[0]


def get_years_played(player: Tuple[str, int, List[str]]) -> int:
    return player[1]


def get_sports(player: Tuple[str, int, List[str]]) -> List[str]:
    return player[2]



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [

]

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    answers = []
    match_exists = False
    answer_exists = False
    for tuple in pa_list:
        if match(tuple[0], src) != None:
            match_exists = True
            answers = tuple[1](match(tuple[0], src))
            if len(answers) >= 1:
                answer_exists = True

    if match_exists == True and answer_exists == False:
        answers.append("No answers")
        return answers
    elif match_exists == False:
        answers.append("I don't understand")
        return answers
    else:
        return answers

