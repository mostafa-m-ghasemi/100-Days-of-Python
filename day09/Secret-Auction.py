def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for i in bidding_dictionary:
        bid_amount = bidding_dictionary[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("*" * 5, "Welcome to the Secret Auction!", "*" * 5)
bids = {}
conyinue_bidding = True
while conyinue_bidding == True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Would you like to continue? (yes/no): ").lower()
    if should_continue == "no":
        conyinue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)





