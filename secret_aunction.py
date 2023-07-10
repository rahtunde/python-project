# from replit import clear
from secret_auct_art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
repeat = True
bid = {}

def higest_bidder(bidder_finder):
  highest_bid = 0
  winner = ""
  
  for highest in bid:
    bidder_amount = bid[highest]
    if bidder_amount > highest_bid:
      highest_bid = bidder_amount
      winner = highest
  print(f"The winner is {winner} with a bid of ${highest_bid}")
      
while repeat:
  name = input("What is your name?: ").lower()
  price = int(input("What is your bid?: $"))
  bid[name] = price
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#   clear()
  if other_bidder == "no":
    repeat = False
    higest_bidder(bid)



  
  