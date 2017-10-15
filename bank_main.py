from Oct2017_Jude.bank_homework.bank_class import bank
import sys

def commands():
    print("""
--- Commands:
[1] Login with an existing account
[2] Create a new account
[3] See existing accounts
[4] Exit""")

def account_commands():
    print("""
[1] Check balance
[2] Deposit
[3] Withdraw
[4] Exit
""")

def main():
    bank_name = bank("Mandiri")
    print(bank_name.getBankName())
    commands()
    while commands != 3:
        x = input()
        if x == "1":
            print("Account list: ")
            bank_name.printCustomers()
            a = int(input("Select a number: ")) - 1
            print("Logged in successfully as" , bank_name.getCustomerName(a))
            while account_commands() != 4:
                y = input()
                if y == "1":
                    print(bank_name.getCustomerBalance(a))
                elif y == "2":
                    b = int(input("Enter amount to deposit: "))
                    bank_name.add_balance(a,b)
                elif y == "3":
                    c = int(input("Enter amount to withdraw: "))
                    bank_name.withdraw(a,c)
                elif y == "4":
                    exit()



        if x == "2":
            a = input("First name: ")
            b = input("Last name: ")
            bank_name.addCustomer(a,b)
        if x == "3":
            bank_name.printCustomers()
        if x == "4":
            exit()

main()
