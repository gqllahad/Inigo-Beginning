import random


uno_card_colors = ["Red Color", "Yellow Color", "Blue Color", "Green Color"]


def card_deck():
    uno_cards = {"Red 0", "Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
                 "Blue 0", "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8", "Blue 9",
                 "Yellow 0", "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7",
                 "Yellow 8", "Yellow 9",
                 "Green 0", "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7", "Green 8",
                 "Green 9", "Wild Draw+4", "Wild Draw+2", "Wild Reverse", "Wild ChangeColor", "Wild Skip"}
    random_uno_cards = list(uno_cards)
    cards = list(random.sample(random_uno_cards, min(7, len(uno_cards))))
    return cards


def center_card():
    random_center_pot = ["Red 0", "Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
                         "Blue 0", "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8",
                         "Blue 9",
                         "Yellow 0", "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7",
                         "Yellow 8", "Yellow 9",
                         "Green 0", "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7",
                         "Green 8",
                         "Green 9"]
    center_pot = random.choice(random_center_pot)
    return center_pot


def random_pick_card():
    uno_cards = {"Red 0", "Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
                 "Blue 0", "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8", "Blue 9",
                 "Yellow 0", "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7",
                 "Yellow 8", "Yellow 9",
                 "Green 0", "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7", "Green 8",
                 "Green 9", "Wild Draw+4", "Wild Draw+2", "Wild Reverse", "Wild ChangeColor", "Wild Skip"}
    random_uno_cards = list(uno_cards)
    random_card = random.sample(random_uno_cards, min(1, len(uno_cards)))
    return random_card


def uno_players():
    number_players = int(input("Enter how many players [2-above] : "))
    while number_players < 2:
        number_players = int(input("Invalid!\nEnter number of players [2-above] : "))
    players = [card_deck() for num in range(number_players)]
    return players


def show_card(players, player_no):
    print("Player ", (player_no + 1), "Hand: ")
    print("_______________")
    for idx, player_hand in enumerate(players, start=1):
        print(f"[{idx}] {player_hand}")
    print("_______________")


def player_out(players):
    for id, player in enumerate(players, start=1):
        if len(player) == 1 and "UNO!" in player:
            print(f"\n\n\t\tCongratulations Player {id} you won!\n\n")
            quit()


def split_color(card):
    color, number = card.split()
    return color


def split_number(card):
    color, number = card.split()
    return number


def split_card(card):
    color, number = card.split()
    return color, number


def same_color_diff_num(card1, card2):
    color1, number1 = split_card(card1)
    color2, number2 = split_card(card2)
    return color1 == color2 and number1 != number2


def diff_color_same_num(card1, card2):
    colour1, num1 = split_card(card1)
    colour2, num2 = split_card(card2)
    return colour1 != colour2 and num1 == num2


def same_card(card1, card2):
    first, second = split_card(card1)
    first_1, second_1 = split_card(card2)
    return first == first_1 and second == second_1


def wild_card_reverse(card):
    wild_split_reverse = split_card(card)
    wild_reverse = wild_split_reverse[1]

    if "Reverse" == wild_reverse:
        return True
    else:
        return False


def wild_card_skip(card):
    wild_split_skip = split_card(card)
    wild_skip = wild_split_skip[1]

    if "Skip" == wild_skip:
        return True
    else:
        return False


def wild_card_draw_plus(players, card, player_turn):
    wild_split_plus = split_card(card)
    wild_card = wild_split_plus[1]

    if "Draw+2" in wild_card:
        for x in range(2):
            players[(player_turn + 1) % len(players)].append(*random_pick_card())
        return card
    elif "Draw+4" in wild_card:
        for x in range(4):
            players[(player_turn + 1) % len(players)].append(*random_pick_card())
        return card
    else:
        return None


def wild_card_change(card, center_card):
    wild_split = split_card(card)
    wild_one = wild_split[1]

    if "ChangeColor" in wild_one:
       return True
    return False


def draw_card(players, deck_cards, center_pot, player_turn):
    while True:
        for idx, card in enumerate(deck_cards, start=1):
            print(f"[{idx}], {card}")
        draw = int(input("Select what card you want to draw (Enter 0 to stop) : "))
        print()
        if draw == 0:
           players[player_turn].append(*random_pick_card())
           break
        elif draw >= 1 and draw <= len(deck_cards):
            draw_card_select = deck_cards[draw - 1]
            if wild_card_change(draw_card_select, center_pot):
                card_select = int(input(
                    "\n[1]Red\n"
                    "[2]Yellow\n"
                    "[3]Blue\n"
                    "[4]Green\n"
                    "\nSelect what color to change : "))
                while card_select > 4 or card_select < 0:
                    card_select = int(input(
                        "\n[1]Red\n"
                        "[2]Yellow\n"
                        "[3]Blue\n"
                        "[4]Green\n"
                        "\nSelect what color you want as default  : (In range 1-4)"))
                if card_select == 1:
                    center_pot = uno_card_colors[0]
                elif card_select == 2:
                    center_pot = uno_card_colors[1]
                elif card_select == 3:
                    center_pot = uno_card_colors[2]
                elif card_select == 4:
                    center_pot = uno_card_colors[3]
                else:
                    print("Invalid")
                print("Changed color!")
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break
            elif wild_card_reverse(draw_card_select):
                print("Reverse!")
                center_pot = draw_card_select
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break
            elif wild_card_skip(draw_card_select):
                print("Skipped")
                center_pot = draw_card_select
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break
            elif wild_card_draw_plus(players, draw_card_select, player_turn):
                card_select = int(input(
                    "\n[1]Red\n"
                    "[2]Yellow\n"
                    "[3]Blue\n"
                    "[4]Green\n"
                    "\nSelect what color you want as default : "))
                while card_select > 4 or card_select < 0:
                    card_select = int(input(
                        "\n[1]Red\n"
                        "[2]Yellow\n"
                        "[3]Blue\n"
                        "[4]Green\n"
                        "\nSelect what color you want as default : (In range 1-4)"))
                if card_select == 1:
                    center_pot = uno_card_colors[0]
                elif card_select == 2:
                    center_pot = uno_card_colors[1]
                elif card_select == 3:
                    center_pot = uno_card_colors[2]
                elif card_select == 4:
                    center_pot = uno_card_colors[3]
                else:
                    print("Invalid")
                print("Deserve! HAHAAAHAHA")
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break

            elif same_color_diff_num(draw_card_select, center_pot):
                print("same color diff number")
                center_pot = draw_card_select
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break

            elif same_card(draw_card_select, center_pot):
                print("same color and same number")
                center_pot = draw_card_select
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break

            elif diff_color_same_num(draw_card_select, center_pot):
                print("diff color same number")
                center_pot = draw_card_select
                deck_cards.pop(draw - 1)
                print("\n\nYou drew : ", draw_card_select)
                print("Card on top of deck : ", center_pot)
                break
            else:
                print("\n\nInvalid! not that close\n")
    return center_pot


def pick_random_card(deck_card, random_card):
    deck_card.extend(random_card)
    return deck_card

def uno_cast(player, player_index):
    if len(player[player_index]) == 2:
        if "UNO!" in player[player_index]:
            print(f"\nPlayer {player_index + 1} already said UNO!\n")
            return

        player[player_index].append("UNO!")
        print(f"\nPlayer {player_index + 1} successfully said UNO!\n")
    else:
        print(f"\nPlayer {player_index + 1} isn't meant the standards!\n")
        return


def shout_uno(player, player_indx):
    you_uno = int(input("Enter Player index to shout on : "))
    if you_uno < 1 or you_uno > len(player) or you_uno == player_indx + 1:
        print("Invalid! Player not found or You can't UNO yourself!")
        return

    if len(player[you_uno - 1]) == 1:
        if "UNO" in player[you_uno - 1]:
            print(f"\nPlayer {player[you_uno]} is safe!\n")
        else:
            for plus_2 in range(2):
                player[you_uno - 1].append(*random_pick_card())
            print("\nIt worked! Player ", you_uno, " received the punishment!\n")
    else:
        print("\nNah! it's too early\n")


def playable_card(player_deck, color, number, player):
    for card in player_deck:
        if "Wild" in card:
            return True
        if color in card or number in card:
            return True
    for players in enumerate(player):
        if len(players) == 1:
            return True
    return False
def uno_actions(players, current_player):
    print("""
    [1]UNO
    [2]Shout UNO to others
    [3] Back
    """)
    gawain = int(input("Enter action you want : "))
    if gawain == 1:
        uno_cast(players, current_player)
    elif gawain == 2:
        shout_uno(players, current_player)
    elif gawain == 3:
        pass



players = uno_players()
cards = card_deck()
center_pot = center_card()
current_color = split_color(center_pot)
current_number = split_number(center_pot)
pick_card = random_pick_card()
player_num = len(players)
player_index = 0

while True:
    show_card(players[player_index], player_index)
    if playable_card(players[player_index], current_color, current_number, players):
        print()
        print("Card on top of deck : ", center_pot)
        print("[1] Draw")
        print("[2] Action")
        print("[3] Pick card")
        action = int(input("Select what action you want to do : "))
        print()
        print()
        if action == 1:
            if player_index >= 0 and player_index < len(players):
                center_pot = draw_card(players, players[player_index], center_pot, player_index)
                reverse = wild_card_reverse(center_pot)
                if reverse:
                    player_index = ((player_index * - 1) + player_num) % player_num
                    card_select_reverse = int(input(
                        "\n[1]Red\n"
                        "[2]Yellow\n"
                        "[3]Blue\n"
                        "[4]Green\n"
                        "\nSelect what color you want as default reverse card : "))
                    while card_select_reverse > 4 or card_select_reverse < 0:
                        card_select = int(input(
                            "\n[1]Red\n"
                            "[2]Yellow\n"
                            "[3]Blue\n"
                            "[4]Green\n"
                            "\nSelect what color you want as default reverse card : (In range 1-4)"))
                    if card_select_reverse == 1:
                        center_pot = uno_card_colors[0]
                    elif card_select_reverse == 2:
                        center_pot = uno_card_colors[1]
                    elif card_select_reverse == 3:
                        center_pot = uno_card_colors[2]
                    elif card_select_reverse == 4:
                        center_pot = uno_card_colors[3]
                    else:
                        print("Invalid")

                skip = wild_card_skip(center_pot)
                if skip:
                    player_index = (player_index + 1) % player_num
                    card_select_skip = int(input(
                        "\n[1]Red\n"
                        "[2]Yellow\n"
                        "[3]Blue\n"
                        "[4]Green\n"
                        "\nSelect what color you want as default reverse card : "))
                    while card_select_skip > 4 or card_select_skip < 0:
                        card_select_skip = int(input(
                            "\n[1]Red\n"
                            "[2]Yellow\n"
                            "[3]Blue\n"
                            "[4]Green\n"
                            "\nSelect what color you want as default reverse card : (In range 1-4)"))
                    if card_select_skip == 1:
                        center_pot = uno_card_colors[0]
                    elif card_select_skip == 2:
                        center_pot = uno_card_colors[1]
                    elif card_select_skip == 3:
                        center_pot = uno_card_colors[2]
                    elif card_select_skip == 4:
                        center_pot = uno_card_colors[3]
                    else:
                        print("Invalid")

                player_index = (player_index + 1) % player_num
        elif action == 2:
            uno_actions(players, player_index)

        elif action == 3:
            pick_random_card(players[player_index], pick_card)
            pick_card = random_pick_card()
            player_index = ((player_index + 1) % player_num)
    else:
        print("\n\nYou are not qualified to play for this round! (automatic +1)!\n\n")
        pick_random_card(players[player_index], pick_card)
        pick_card = random_pick_card()
        player_index = (player_index + 1) % player_num

    player_out(players)

