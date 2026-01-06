import os

# logo replacement (since art module may not exist)
logo = """
 ____  _     ___ ____  
| __ )| |   |_ _|  _ \ 
|  _ \| |    | || | | |
| |_) | |___ | || |_| |
|____/|_____|___|____/ 
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print(logo)

bids = {}
bidding_finish = False
highest_bid = 0
winner = ""

def find_highest_bidder(bidding_record):
    global highest_bid, winner
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finish:
    name = input("what is your name? ")
    price = int(input("what is your bid? $"))
    bids[name] = price

    should_continue = input("are there any other bidders? type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()


