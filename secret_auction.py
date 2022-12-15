def find_highest_bidder(bids):
    highest_bid=0
    highest_bidder=''
    for person in bids:
        if bids[person]>highest_bid:
            highest_bid=bids[person]
            highest_bidder=person
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

bids={}
restart = True
while restart:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?$"))
    bids.update({name:bid})
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if restart =='no':
        restart = False
        find_highest_bidder(bids)


