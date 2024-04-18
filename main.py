"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
  value_one = value_of_card(card_one)
  value_two = value_of_card(card_two)

  if value_one == value_two:
    return card_one, card_two
  elif value_one < value_two:
    return card_two
  else:
    return card_one


def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if card_one == "A" or card_two == "A":
        return 1
    elif value_one + value_two <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    if (card_one == "A" and (card_two == "10" or card_two == "K" or card_two == "Q" or card_two == "J")) \
            or (card_two == "A" and (card_one == "10" or card_one == "K" or card_one == "Q" or card_one == "J")):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    total_value = value_one + value_two

    if total_value in [9, 10, 11]:
        return True
    else:
        return False
