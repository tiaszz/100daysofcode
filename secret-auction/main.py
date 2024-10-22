from art import logo


from os import system

print(logo)

keep_bidding = True
bid = {}


def find_highest_bid(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The highest bid is {highest_bid}. Made by {winner}")


while keep_bidding:
    name = input("Bidder's name: ")
    bid_value = int(input("Bid price: "))

    bid[name] = bid_value

    keep_going = input("Do you want to continue? 'yes' / 'no'\n")
    system("clear")

    if keep_going == "no":
        find_highest_bid(bid)
        keep_bidding = False
