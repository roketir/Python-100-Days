from replit import clear
from art import logo

print(logo)

bids = {}
keep_bidding = True

def find_highest_bid_price(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
      amount =  bidding[bidder] 
      if amount > highest_bid:
        highest_bid = amount
        winner = bidder
    return print(f'The winner is {winner} with a bid of ${highest_bid}')


while keep_bidding == True:

    name = input("Please enter your name: ")
    bid_amount = int(input("please enter you bid amount: $"))
    bids[name] = bid_amount
    another_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if another_bidders == 'yes':
        keep_bidding = True
        clear()
    else:
        keep_bidding = False
        find_highest_bid_price(bids)