from typing import Union, Literal

def win(opp: Union[Literal['A'], Literal['B'], Literal['C']], you: Union[Literal['X'], Literal['Y'], Literal['Z']]) -> int:
    if ord(opp) - ord("A") == ord(you) - ord("X"):
        return 3
    return 6 if opp == 'A' and you == 'Y' or opp == 'B' and you == 'Z' or opp == 'C' and you == 'X' else 0

def score(you: Union[Literal['X'], Literal['Y'], Literal['Z']]) -> int:
    return ord(you) - ord("X") + 1

def strategy_score(opp, strategy) -> int:
    win_score = 0
    shape = 0
    if strategy == "X":
        win_score = 0
        shape = (ord(opp) - ord("A") - 1) % 3 + 1
    elif strategy == "Y":
        win_score = 3
        shape = ord(opp) - ord("A") + 1
    elif strategy == "Z":
        win_score = 6
        shape = (ord(opp) - ord("A") + 1) % 3 + 1
    return win_score + shape

print(sum(win(opp, you) + score(you) for opp, you in (match.split(" ") for match in open("input.txt").read().strip().split("\n"))))
print(sum(strategy_score(opp, strategy) for opp, strategy in (match.split(" ") for match in open("input.txt").read().strip().split("\n"))))
