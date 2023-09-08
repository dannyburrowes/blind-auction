import os
from art import logo

print(logo)
another_bidder = True
bid_dictionary = {}


def key_with_max_val(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def max_val(d):
    v = list(d.values())
    return max(v)


while another_bidder:
    name = input("Name?\n")
    bid_price = input("Bid price?\n")
    bid_dictionary[name] = bid_price
    other_bidders = input("Add another bidder? y or n\n")
    if other_bidders == "n":
        another_bidder = False
    elif other_bidders == "y":
        os.system('cls')
    else:
        another_bidder = False
        print("Invalid input")

os.system('cls')
print(f"The highest bidder is {key_with_max_val(bid_dictionary)} with a bid of £{max_val(bid_dictionary)}.")