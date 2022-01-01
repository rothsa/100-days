from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

auction_bids = {}

def enter_bid():
    name = ""
    bid = ""
    name = input("What is your name: ")
    bid = int(input("What is your bid? "))
    auction_bids[name] = bid

def find_high_bid():
    print(auction_bids)
    print(max(auction_bids, key=auction_bids.get))

auction_end = "y"

while auction_end == "y":
    enter_bid()
    auction_end = input("Enter y and hit enter to add a bid: ")
    if auction_end == "y":
        clear()
    else:
        find_high_bid()



    
