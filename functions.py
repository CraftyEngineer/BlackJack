import random
def deal_cards(cards):
  dealt_card=random.choice(cards)
  return(dealt_card)


def calculate_score(list_of_cards):
  if sum(list_of_cards)==21:
    return 0
  elif sum(list_of_cards)>21:
    for card in list_of_cards:
      if card==11:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return(sum(list_of_cards))
  else:
    return(sum(list_of_cards))


def compare_score(user_score, computer_score):
  if user_score==0:
    print("You have won!")
  elif computer_score==0:
    print("Dealer has won!")
  elif computer_score>21:
    print("You have won!")
  elif user_score>21:
    print("Dealer has won")
  elif user_score>computer_score:
    print("You have won!")
  elif user_score<computer_score:
    print("Dealer has won!")