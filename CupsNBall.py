def A(pos):     # This defines the swapping for A and B positions
    pos[0], pos[1] = pos[1], pos[0]

def B(pos):     # This defines the swapping for B and C positions
    pos[1], pos[2] = pos[2], pos[1]

def C(pos):     # This defines the swapping for A and C positions
    pos[0], pos[2] = pos[2], pos[0]

def main():
    pos = ["ball_pos","first_pos","second_pos"] # This is the initial position of the cups. The ball is in the first one.
    alphabets = input("Input the alphabets: ")
    alphabets = list(alphabets.upper())
    for x in alphabets:     # The ball position will be shuffled based on the input alphabets
        if x == "A":
            A(pos)
        if x == "B":
            B(pos)
        if x == "C":
            C(pos)
    final_result = pos.index("ball_pos")
    print("The final position of the ball is:",final_result+1)   # +1 is added because indexes start from 0

main()
