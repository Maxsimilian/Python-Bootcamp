from replit import clear
from art import logo
print(logo)
#Dictionaries
auction_dictionary = {}

#Define function

def auction(name, bid):
  auction_dictionary[name] = bid

def highest_bid():
  sum = 0
  bidder = ""
  for name in auction_dictionary:
    value = auction_dictionary[name]
    if value > sum:
      sum = value
      bidder = name
  print(f"The highest bid of the auction is {bidder} with a bid of ${sum}.")

  
blind_auction = False
while not blind_auction:
  
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  auction(name, bid)
  question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if question == "yes":
    clear()
    auction(name, bid)
  elif question == "no":
    blind_auction = True
    highest_bid()
  


  
