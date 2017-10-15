from Oct2017_Jude.bank_homework.customer_class import Customer

class bank:
    def __init__(self,bankName):
        self.bankName = str(bankName)
        self.customers = []
        self.customers_length = 0

    def printCustomers(self):
        for i in range (self.customers_length):
            print(self.customers[i].getFirstName(), self.customers[i].getLastName())

    def getBankName(self):
        return self.bankName

    def getCustomers(self):
        return self.customers

    def addCustomer(self, first, last):
        x = first+last
        counter = 0
        if self.customers_length == 0:
            self.customers.append(Customer(first, last))
            self.customers_length += 1
            print("Successfully added customer")
        else:
            for i in range (self.customers_length):
                if x == self.customers[i].getFirstName()+self.customers[i].getLastName():
                    counter += 1
                else:
                    continue
            if counter > 0:
                print("Error. Customer already exist.")
                return False
            else:
                self.customers.append(Customer(first, last))
                self.customers_length += 1
                print("Successfully added customer")

    def getNumberOfCustomers(self):
        return self.customers_length

    def getCustomerName(self,num):
        return "{} {}".format(self.customers[int(num)].getFirstName(), self.customers[int(num)].getLastName())

    def getCustomerBalance(self,num):
        return "Balance: {}".format(self.customers[int(num)].getAccount())

    def add_balance(self,num,value):
        self.customers[int(num)].customer_deposit(value)

    def withdraw(self,num,value):
        self.customers[int(num)].customer_withdraw(value)
