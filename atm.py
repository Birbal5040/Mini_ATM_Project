class Atm:
    
    # Constructor function
    def __init__(self):
        self.pin="1234"
        self.balance=0
        self.menu()
    def menu(self):
        User_input=input("""Hello how would you like to proceed?
        
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit\n           """)
        
        if User_input=="1":
            self.create_pin()
        elif User_input=="2":
            self.deposit()
        elif User_input=="3":
            self.withdraw()
        elif User_input=="4":
            self.check_balance()
        else:
            print("bye")
    def create_pin(self):
        self.pin=input("Enter your 4 digit pin: ")
        print("pin set successfully\n")
        print("you are want to some operation again. if yes then type y not then type n \n")
        ent=input("Enter  what you want to do? : ")
        if ent=="y" or ent=="Y":
            self.menu()
        else:
            print("bye")
        
    def deposit(self):
        temp=input("Please enter your pin number: ")
        if temp==self.pin:
            amount=int(input("Please enter the amount to deposit :"))
            self.balance+=amount
            print("balance deposit successfully\n")
        else:
            print("Invalid pin number\n")
        print("you are want to some operation again. if yes then type y not then type n \n")
        ent=input("Enter  what you want to do? : ")
        if ent=="y" or ent=="Y":
            self.menu()
        else:
            print("bye")
       
            
    def withdraw(self):
        temp=input("Please enter your pin number: ")
        if temp==self.pin:
            amount=int(input("Please enter the amount to withdraw : "))
            if amount<=self.balance:
                self.balance-=amount
                print("balance withdraw successfully\n")
            else:
                print("insufficient funds\n")
        else:
            print("Invalid pin number\n")
        print("you are want to some operation again. if yes then type y not then type n \n")
        ent=input("Enter  what you want to do? : ")
        if ent=="y" or ent=="Y":
            self.menu()
        else:
            print("bye")
    def check_balance(self):
        temp=input("Please enter your pin number: ")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid pin number\n")
        print("you are want to some operation again. if yes then type y not then type n \n")
        ent=input("Enter  what you want to do? : ")
        if ent=="y" or ent=="Y":
            self.menu()
        else:
            print("bye")





sbi=Atm()
# sbi.create_pin()
# sbi.deposit(50000)
# sbi.withdraw(25000)
# sbi.check_balance()
