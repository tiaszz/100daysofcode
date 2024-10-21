from art import logo


print(logo)

keep_bidding = True

while keep_bidding:
    name = input("Bidder's name: ")
    bid_value = int(input("Bid price: "))
    bid = {}

    bid[name] = bid_value
    print(bid)

    keep_going = input("Wanna continue?")

    if keep_bidding == "no":
        keep_bidding = False
