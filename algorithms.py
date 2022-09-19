from itertools import combinations


def pair_check(deck: list):
    deck.sort(key=lambda x: x[0])
    for i in range(1, len(deck)):
        if deck[i][0] == deck[i-1][0]:
            return True
    return False


def two_pair_check(deck: list):
    deck.sort(key=lambda x: x[0])
    calc = 0
    pairs = set()
    for i in range(1, len(deck)):
        if deck[i][0] == deck[i-1][0] and deck[i][0] not in pairs:
            calc += 1
            pairs.add(deck[i][0])
    if calc < 2:
        return False
    return True


def pair_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if pair_check(new_deck):
            calc += 1
    return calc / len(choice)


def two_pair_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if two_pair_check(new_deck):
            calc += 1
    return calc / len(choice)


def set_check(deck: list):
    deck.sort(key=lambda x: x[0])
    i = 1
    while i < len(deck):
        if deck[i][0] == deck[i-1][0]:
            count = 0
            while i < len(deck) and deck[i][0] == deck[i-1][0]:
                count += 1
                i += 1
            if count == 2:
                return True
        i += 1
    return False


def kare_check(deck: list):
    deck.sort(key=lambda x: x[0])
    deck.sort()
    i = 1
    while i < len(deck):
        if deck[i][0] == deck[i - 1][0]:
            count = 0
            while i < len(deck) and deck[i][0] == deck[i - 1][0]:
                count += 1
                i += 1
            if count == 3:
                return True
        i += 1
    return False


def set_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if set_check(new_deck):
            calc += 1
    return calc / len(choice)


def kare_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if kare_check(new_deck):
            calc += 1
    return calc / len(choice)


def straight_check(deck: list):
    deck.sort(key=lambda x: x[0])
    deck.sort()
    i = 1
    while i < len(deck):
        if deck[i][0] - deck[i - 1][0] == 1:
            count = 0
            while i < len(deck) and deck[i][0] - deck[i - 1][0] == 1:
                count += 1
                i += 1
            if count == 4:
                return True
        i += 1
    return False


def straight_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if straight_check(new_deck):
            calc += 1
    return calc / len(choice)


def flush_check(deck: list):
    suits = {1: 0, 2: 0, 3: 0, 4: 0}
    for el in deck:
        suits[el[1]] += 1
    max_suit = max(suits.values())
    if max_suit < 5:
        return False
    return True


def flush_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if flush_check(new_deck):
            calc += 1
    return calc / len(choice)


def full_house_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if full_house_check(new_deck):
            calc += 1
    return calc / len(choice)


def full_house_check(deck: list):
    deck.sort(key=lambda x: x[0])
    i = 1
    flag = False
    while i < len(deck):
        if deck[i][0] == deck[i-1][0]:
            count = 0
            while i < len(deck) and deck[i][0] == deck[i-1][0]:
                count += 1
                i += 1
            if count == 2:
                three = deck[i-1][0]
                flag = True
                break
        i += 1
    if not flag:
        return False
    for i in range(1, len(deck)):
        if deck[i][0] == deck[i-1][0] and deck[i][0] != three:
            return True
    return False


def straight_flush_check(deck: list):
    suits = {1: 0, 2: 0, 3: 0, 4: 0}
    for el in deck:
        suits[el[1]] += 1
    max_suit = max(suits.values())
    if max_suit < 5:
        return False
    else:
        suit = max(suits, key=suits.get)
    new_deck = []
    for el in deck:
        if el[1] == suit:
            new_deck.append(el)
    return straight_check(new_deck)


def straight_flush_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if straight_flush_check(new_deck):
            calc += 1
    return calc / len(choice)


def flush_royal_check(deck: list):
    suits = {1: 0, 2: 0, 3: 0, 4: 0}
    for el in deck:
        suits[el[1]] += 1
    max_suit = max(suits.values())
    if max_suit < 5:
        return False
    else:
        suit = max(suits, key=suits.get)
    new_deck = []
    for el in deck:
        if el[1] == suit:
            new_deck.append(el[0])
    new_deck = set(new_deck)
    for i in range(9, 14):
        if i not in new_deck:
            return False
    return True


def flush_royal_posibility(deck: list):
    calc = 0
    whole_deck = [(x, y) for x in range(1, 14) for y in range(1, 5)]
    new_deck = list(set(whole_deck) - set(deck))
    new_deck.sort()
    choice = list(combinations(new_deck, 7 - len(deck)))
    for el in choice:
        new_deck = deck[:]
        for i in range(7 - len(deck)):
            new_deck.append(el[i])
        if flush_royal_check(new_deck):
            calc += 1
    return calc / len(choice)


# deck = [(1, 3), (9,3)]
# print(pair_posibility(deck))
# print(two_pair_posibility(deck))
# print(set_posibility(deck))
# print(straight_posibility(deck))
# print(flush_posibility(deck))
# print(full_house_posibility(deck))
# print(kare_posibility(deck))
# print(straight_flush_posibility(deck))
# print(flush_royal_posibility(deck))