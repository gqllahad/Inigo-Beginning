import random


def deck_cards():
  deck = []
  between_cards = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
  random_cards = list(between_cards)
  cards_to_deck = list(random.sample(random_cards, min(2, len(between_cards))))
  deck.extend(cards_to_deck)
  random.shuffle(deck)
  return deck


def player_life_points():
    return 30


def player_out(gamer):
    for player in gamer:
        if player[1] <= 0:
            print(f"Goodbye Player {gamer.index(player)+1} is out!")
            gamer.pop(gamer.index(player))
    if len(gamer) == 1:
        print(f"\n\n\t\t\tYou win! Player {gamer.index(gamer[0])+1} Congratulations!")
        return False
    return True


def system_card():
    between_cards = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
    random_cards = list(between_cards)
    system_choice = random.sample(random_cards, 1)[0]
    return system_choice


def show_card(player_turn, player_num):
    num_player = len(player_num)
    player_index = player_turn % num_player
    print("\n\nPlayer {}".format(player_turn+1))
    print("Your Hand : ")
    for x in range(2):
        print(*player_num[0][x], end="\n  ")
    print("\nPoints : ", player_num[1])
    print()


def card_checker(card1, card2, center_card):
    letter_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                     '9': 9, '10': 10}
    if card1 and card2 and center_card in letter_values:
        if letter_values[center_card] <= letter_values[card1] and letter_values[center_card] > letter_values[card2]:
            print("Holemole :0!!!")
            return True
        elif letter_values[center_card] > letter_values[card1] and letter_values[center_card] <= letter_values[card2]:
            print("Damn!")
            return True
        elif letter_values[card1] == letter_values[card2] and letter_values[card2] == letter_values[card1]:
            same_card = input("Higher/Lower : ").capitalize()
            if same_card == "Higher":
                if letter_values[center_card] > letter_values[card1] and letter_values[card2]:
                    return True
                elif letter_values[center_card] < letter_values[card1] and letter_values[card2]:
                    return False
            elif same_card == "Lower":
                if letter_values[center_card] < letter_values[card1] and letter_values[card2]:
                    return True
                elif letter_values[center_card] > letter_values[card1] and letter_values[card2]:
                    return False
        else:
            print("Not in the scope! olats")
            return False
    else:
        print("No scopes!")
        return False

def player():
    print("This Game : Shows If card 1 is higher than center card you win if not u lose")
    number_of_players = int(input("Enter number of players : "))
    while number_of_players < 2:
        number_of_players = int(
            input("Invalid! Please enter 2 or more players! \n Enter number of players : "))
    players = [[deck_cards(), player_life_points()] for num in range(number_of_players)]
    return players

def action_bet(players):
    bet_player = int(input(f"Enter points you want to gamble Points : [{players[1]}] : "))
    while bet_player > players[1]:
        print("Wtf you input more than your points! TRY AGAIN!")
        bet_player = int(input(f"Enter points you want to gamble Points : [{players[1]}] : "))
    if card_checker(players[0][0], players[0][1], system_card()) == True:
        print("`````!!! CONGRATS! GAMBLER !!! `````")
        players[1] += bet_player
    else:
        print("Fuck!")
        players[1] -= bet_player






players = player()
playing = True
num_players = len(players)
player_turn = random.randint(0, num_players-1)
while playing:
  system_select = system_card()
  players = [[deck_cards(), life] for x, life in players]
  show_card(player_turn, players[player_turn])

  actions = input("Enter player's move [Bet][Refuse] : ").capitalize()
  if actions == "Bet":
      if players[player_turn][0][0] == players[player_turn][0][1]:
          same_card = input("Higher/Lower : ").capitalize()
          action_bet(players[player_turn])
          player_turn = (player_turn + 1) % num_players
          print("System Choice ; ", system_select)
      else:
          action_bet(players[player_turn])
          player_turn = (player_turn + 1) % num_players
          print("System Choice ; ", system_select)
  elif actions == "Refuse":
      print("System Choice ; ", system_select)
      pass
      player_turn = (player_turn + 1) % num_players
  playing = player_out(players)
