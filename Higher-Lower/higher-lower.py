from art import logo
from art import vs
from game_data import data
from replit import clear
import random
print(logo)
# Globals
Score = 0    
    
def Game():
  global Score
  compare_a  = random.choice(data)
  list_of_items_a = list(compare_a.values())
  end_game = False
  while not end_game:
    follower_a = int(list_of_items_a[1])
    print(f"Compare A: {list_of_items_a[0]}, a {list_of_items_a[2]}, from {list_of_items_a[3]}.")
    print(vs)
    compare_b  = random.choice(data)
    while compare_a == compare_b:
      compare_b = random.choice(data)
    list_of_items_b = list(compare_b.values())
    follower_b = int(list_of_items_b[1])
    print(f"Compare B: {list_of_items_b[0]}, a {list_of_items_b[2]}, from {list_of_items_b[3]}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_answer == "a":
      if follower_a > follower_b:
        clear()
        Score += 1
        print(f"You're right! Current score: {Score}.")
        list_of_items_a = list_of_items_a
        
      else:
        clear()
        end_game = True
        print(f"Sorry, that's wrong. Final Score: {Score}")
        
    elif user_answer == "b":
      if follower_b > follower_a:
        clear()
        Score +=1
        print(f"You're right! Current score: {Score}.")
        list_of_items_a = list_of_items_b
        
      else:
        clear()
        end_game = True
        print(f"Sorry, that's wrong. Final Score: {Score}")

Game()
  
