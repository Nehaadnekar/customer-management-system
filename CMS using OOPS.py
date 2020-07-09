#CMS using oops:

# Business Logic Layer(BLL):



class Customer:
    cusList = []

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0
        self.address = 0
        self.pin = 0
        self.state = 0

    def addCust(self):
        Customer.cusList.append(self)

    def searchCust(self):
        for e in Customer.cusList:

            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.address = e.address
                self.state = e.state
                self.pin = e.pin
                return

    def deleteCust(self):
        for e in Customer.cusList:
            if e.id == self.id:
                Customer.cusList.remove(e)
                return

    def updateCust(self):
        for e in Customer.cusList:
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address = self.address
                e.state = self.state
                e.pin = self.pin
                return
            else:
                print("Customer ID Does'nt Exist! Please Enter a Valid ID...")
                updateCust()


# Presentation Layer(PL):
def displayCust(cus):
    print(f"Customer ID : {cus.id}   ,   Customer Name: {cus.name}")
    print(f"Customer age : {cus.age}  ,    Customer Mobile No: {cus.mob}")
    print(f"Customer State: {cus.state}")
    print(f"Customer Address : {cus.address} ,     Customer Address PINCODE: {cus.pin}")


def userAge():
    age = input("Enter User's Age: ")
    if age.isdecimal():
        if int(age) >= 1 and int(age) <= 105:
            return age
        else:
            print("Enter a valid age!")
            userAge()
    else:
        print("enter age in digits only")
        userAge()



def userMob():
    mob = input("Enter User's Valid 10 Digit Mobile Number: ")
    if mob.isdecimal():
        if len(mob) == 10:
            return mob
        else:
            print("Enter a valid mobile number!")
            userMob()
    else:
        print("enter digits only")
        userMob()


def userPin():
    pin = input("Enter Address PINCODE: ")
    if pin.isdecimal():
        if len(pin) == 6:
            return pin
        else:
            print("Enter a Valid PINCODE!")
            userPin()
    else:
        print("enter digits only")
        userPin()

while (1):
    print("Welcome to my Customer Management System!")
    print("press: 1 for Add Customer, 2 For Searching/Displaying a Particular Customer")
    print("3 for Delete Customer, 4 For Update/Modify a Particular Customer")
    print("5 for Display All Customers, 6 For Exit this CMS")
    choice = input("Enter the choice : ")
    if choice == "1":
        cus = Customer()
        cus.id = input("Enter Customer ID: ")
        for e in Customer.cusList:
            if cus.id == e.id:
                print("ID Alerady Exists!")
                cus.id=input("enter  your unique customer ID:")

        cus.name = input("Enter Customer Name: ")
        cus.address = input("Enter Valid Customer Address: ")
        cus.state = input("Enter Customer State: ")
        cus.age = userAge()
        cus.mob = userMob()
        cus.pin = userPin()
        cus.addCust()

        print("Customer Added Successfully!")


    elif choice == "2":
        cus = Customer()
        cus.id = input("Enter User ID to Display it's Data: ")
        for e in Customer.cusList:
            if cus.id != e.id:
                cus.searchCust()
                displayCust(cus)


            else:
                print("Customer ID Does'nt Exist! Please Enter a Valid ID...")
                cus.id = input("Enter User ID to Display it's Data: ")


    elif choice == "3":
        cus = Customer()
        cus.id = input("Enter Customer ID: ")
        for e in Customer.cusList:
            if cus.id != e.id:
                print("Customer ID Does'nt Exist! Please Enter a Valid ID...")
            else:
                cus.deleteCust()
                print("Customer Deleted Successfully!")

    elif choice == "4":
        cus = Customer()
        cus.id = input("Enter Customer ID: ")
        for e in Customer.cusList:
            if cus.id != e.id:
                print("Customer ID Does'nt Exist! Please Enter a Valid ID...")
                cus.id=input("enter a valid ID:")

            else:
                cus.updateCust()
        cus.name = input("Enter Customer Updated Name: ")
        cus.address = input("Enter Updated Customer Address: ")
        cus.state = input("Enter Customer Updated State: ")
        cus.age = input("Enter Customer Updated Age: ")
        cus.dob = input("Enter Customer Updated Date Of Birth: ")
        cus.mob = input("Enter Customer Updated Mobile Number: ")
        cus.pin = input("Enter Customer Updated PINCODE: ")
        print("Customer ID Does'nt Exist! Please Enter a Valid ID...")


    elif choice == "5":

        for e in Customer.cusList:
            displayCust(cus)

    elif choice == "6":

        print("Thanks for Using my CMS!")

        break
