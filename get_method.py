import algorithms as alg


def get_number_fromL(ch: str):
    if ch == 'H':
        return 1
    if ch == 'S':
        return 2
    if ch == 'D':
        return 3
    if ch == 'C':
        return 4

def get_number_from_number(ch: str):
    if ch == 'J':
        return 10
    elif ch == 'Q':
        return 11
    elif ch == 'K':
        return 12
    elif ch == 'A':
        return 13
    else:
        return int(ch) - 1


def read(deck_from_js: list):
    deck = list()
    for el in deck_from_js:
        num1, num2 = get_number_from_number(el[:-1]), get_number_fromL(el[-1])
        deck.append((num1, num2))
    return deck


def process(deck):
    deck = read(deck)
    print(deck)
    print(alg.pair_posibility(deck))
    results = {
        'pair': alg.pair_posibility(deck),
        '2pairs': alg.two_pair_posibility(deck),
        '3kind': alg.set_posibility(deck),
        '4kind': alg.kare_posibility(deck),
        'straight': alg.straight_posibility(deck),
        'flush': alg.flush_posibility(deck),
        'fullhouse': alg.full_house_posibility(deck),
        'straight_flush': alg.straight_flush_posibility(deck),
        'royal_flush': alg.flush_royal_posibility(deck),
    }
    return results

