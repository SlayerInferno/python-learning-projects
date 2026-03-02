from secret_auction_art import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
    # Basic self implemented way to find the Highest bid
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidders = {}
more_bids = True
while more_bids:
    bidder = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    bidders[bidder] = bid

    if input("Are there more bidders?(Y/N): ").lower() != "y":
        more_bids = False
    else:
        print("\n"*20)      #To clear screen
find_highest_bidder(bidders)