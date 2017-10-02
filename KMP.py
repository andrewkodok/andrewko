#This function is to put the string input into a list and seperate them based on the dash
def stripped(x):
    return x.split("-")

def main():
    x = input("Author: ")
    name = stripped(x)
    for i in name:
        print(i[0].title(), end="")
        # Only the first Uppercased letter will be printed after being seperated using stripped function
        # 'end="" ' is to print the letters side by side
main()
