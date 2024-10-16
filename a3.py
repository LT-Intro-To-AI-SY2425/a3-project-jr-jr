from players import player_db
from match import match
from typing import List, Tuple, Callable, Any



def get_name(player: Tuple[str, int, List[str], List[str]]) -> str:
    return player[0]


def get_years_played(player: Tuple[str, int, List[str], List[str]]) -> int:
    return player[1]


def get_sports(player: Tuple[str, int, List[str], List[str]]) -> List[str]:
    return player[2]

def get_teams(player: Tuple[str, int, List[str], List[str]]) -> List[str]:
    return player[3]



def years_by_name(matches: List[str]) -> List[str]:
    years = []
    for player in player_db:
        if get_name(player) == matches[0]:
            years.append(str(get_years_played(player)))

    return years

def players_by_year(matches: List[str]) -> List[str]:
    players = []

    for player in player_db:
        if get_years_played(player) == int(matches[0]):
            players.append(get_name(player))
    
    return players

def players_by_sport(matches: List[str]) -> List[str]:
    players = []
    for player in player_db:
        for sport in get_sports(player):
            if sport == matches[0]:
                players.append(get_name(player))
    return players




pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    
    (str.split("how many years did % play"), years_by_name),
    (str.split("what players played _ years"), players_by_year),
    (str.split("what players played _"), players_by_sport),

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





print(search_pa_list(["what", "players", "played", "Basketball"]))