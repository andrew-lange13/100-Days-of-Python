# from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

auction_dictionary = {}

print("Welcome to the secret auction program.")

continue_auction = True

while continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "yes":
        continue_auction = True
        # clear()
    else:
        continue_auction = False
        # clear()


# print(auction_dictionary)

high_bid = max(auction_dictionary.values())
high_bidder = max(auction_dictionary, key=auction_dictionary.get)
print(f"The winning bidder is {high_bidder} with a bid of ${high_bid}")

