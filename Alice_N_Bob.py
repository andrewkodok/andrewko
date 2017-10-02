print("Alice's and Bob's a Game of Stones")
print("Enter Number: " , end="")
x = int(input ())

def main():
    if x%2 == 0:        # This is to find out if the number is odd or even
        print ("Bob")   # Bob will win if the number has no remainder, as it is an even number

    else:
        print ("Alice") # Alice wins if the number has a remainder, as it is an odd number

main()
