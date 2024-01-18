import sys, subprocess

bids = {}
is_done = False

def lets_bid(name, amount):
  bids[name] = amount

def highest_bid():
  high = 0 
  winner = ""
  for bidder in bids:
    if bids[bidder] > high:
      high = bids[bidder]
      winner = bidder
  
  print(f"The highest bidder was {winner} with ${high}")

while not is_done:
  name = input("What is your name?\n")
  amount = int(input("What is your bid amount?\n$"))
  more_bidders = input("Are there more bidders? Type y or n\n")
  lets_bid(name, amount)
  if more_bidders == "n":
    subprocess.run("clear", shell=True)
    highest_bid()
    is_done = True
  else:
    subprocess.run("clear", shell=True)