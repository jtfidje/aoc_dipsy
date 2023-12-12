from solver import utils
from collections import Counter


def solve(input_file: str):
    lines = [x.split() for x in utils.read_lines(input_file)]
    hand_types = {"5": [], "4": [], "32": [], "3": [], "22": [], "2": [], "1": []}

    for line in lines:
        hand = line[0]
        count = Counter(hand)
        count_no_j = Counter(list(filter(lambda x: x != "J", hand)))

        if("J" in count and count["J"] < 5):
            top_count = count_no_j.most_common(1)[0][0]
            count[top_count] += count["J"]
            count["J"] = 0

        hand_type = ""
        for card, card_count in count.most_common(2):
            if card_count > 1:
                hand_type += str(card_count)

        if hand_type == "":
            hand_type = "1"

        lexographic_hand = hand
        lexo_map = {"A": "Z", "K": "Y", "Q": "X", "J": "!", "T": "V"}
        for char, initial in lexo_map.items():
            lexographic_hand = lexographic_hand.replace(char, initial)

        hand_types[hand_type].append((lexographic_hand, int(line[1])))

    order = []
    for hand_type, hands in hand_types.items():
        if len(hands) == 0:
            continue
        for hand in sorted(hands, reverse=True):
            order.append(hand[1])

    max_rank = len(order)
    winnings = []
    for i, bid in enumerate(order):
        winnings.append((max_rank - i) * bid)

    return sum(winnings)