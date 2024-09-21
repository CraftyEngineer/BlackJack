import random
import art
import functions as func
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.blackjack_art)
user_cards = []
computer_cards = []


for i in range(0,2):
  user_cards.append(func.deal_cards(cards))
for i in range(0,2):
  computer_cards.append(func.deal_cards(cards))
user_score=func.calculate_score(user_cards)
computer_score=func.calculate_score(computer_cards)
if user_score==0 and computer_score==0:
  print("The Dealer also had a blackjack, you lost!")
  not_win=False
elif user_score==0:
  print("You have a blacjack. Congratulations, you win!")
  not_win=False
elif computer_score==0:
  print("Dealer had a blacjack. Uh-oh, you lost!")
  not_win=False
elif computer_score>21:
  print("You have won!")
  not_win=False
elif user_score>21:
  print("Dealer has won")
  not_win=False
else:
  not_win=True

print(user_cards)
print(f"User score= {func.calculate_score(user_cards)}")
print(f"The first computer card is: {computer_cards[0]}")



while not_win:
  draw=True
  while draw:
    choice=input("Do you want to draw another card? ").lower()
    if choice=="yes":
      user_cards.append(func.deal_cards(cards))
      user_score=func.calculate_score(user_cards)
      print(user_cards)
      print(f"user's current score is= {user_score}")
      if user_score>21:
        print("Uh oh! you went over, you lost!")
        draw=False
        not_win=False
      elif user_score==0:
        print("You won!")
        draw=False
        not_win=False
    else:
      while computer_score<=17 and computer_score<21 and computer_score!=0:
        computer_cards.append(func.deal_cards(cards))
        computer_score=func.calculate_score(computer_cards)


      func.compare_score(user_score, computer_score)
      print(f"The final computer score was: {computer_score}")
      print(f"and the final computer's hand was: {computer_cards}")
      draw=False
      not_win=False
