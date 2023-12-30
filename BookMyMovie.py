'''
This project gets you know how do you virtually select a Ticket and book it, how it does not show the seats which are
booked and how it cuts cost according to certain scenarios for certain seats and rows
This will ask the number of rows and number of seats per row and then show 4 options which are listed below.
1.Show the seats
2. Buy a Ticket
3. Statistics
4. Show booked Tickets User Info
0. Exit
'''


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Theatre:
    def __init__(self, rows, cols):
        self.totalIncome = 0
        self.no_of_purchased_tickets = 0
        self.current_income = 0
        self.vacant_seats = (rows * cols)
        self.rows = rows
        self.cols = cols
        self.seats = []
        for row in range(rows):
            seats_in_row = []
            for col in range(cols):
                seat_price = self.get_price(row)
                seats_in_row.append(Seat(seat_price))
                self.totalIncome += seat_price
            self.seats.append(seats_in_row)

    def get_price(self, row):
        if self.rows * self.cols <= 60:
            return 10
        elif (self.rows // 2) <= row:
            return 8
        else:
            return 10

    def print_seats(self):
        line_no = 0
        for row in range(self.rows + 1):
            if line_no == 0:
                print(" ", end=" ")
            else:
                print(str(line_no), end=" ")
            for col in range(1, self.cols + 1):
                if row == 0:
                    print(col, end=" ")
                elif self.seats[row - 1][col - 1].person is None:
                    print("s", end=" ")
                else:
                    print("b", end=" ")
            print()
            line_no = line_no + 1

    def book_ticket(self):
        row = int(input("Enter the Row Number you want to book \n")) - 1
        col = int(input("Enter the Column Number you want to book \n")) - 1
        if row >= self.rows or col > self.cols:
            print("Theatre capacity is less then the seat or row number you are trying to book please try again.")
        elif self.seats[row][col].person is not None:
            print("already booked")
        else:
            print(Color.GREEN + Color.BOLD + "Price for the seat you are booking is: $" + Color.END,
                  self.seats[row][col].price)
            option1 = "yes"
            option2 = "no"
            k = input(Color.BOLD + "Please confirm yes to continue and no to return to menu: " + Color.END)
            print()
            if k == option1:
                person = Person(input("Enter the your name: "), input("Enter your Gender M/F: "),
                                int(input("Enter your age: ")), int(input("Enter your phone number: ")))
                self.seats[row][col].person = person
                print(Color.GREEN + Color.BOLD + "Booked Successfully" + Color.END)
                self.no_of_purchased_tickets += 1
                self.current_income += self.seats[row][col].price
                print()
            elif option == 2:
                print(Color.BOLD + "Thanks for visiting." + Color.END)
                print()
                menu()
            else:
                print("you might be entering yes in upper case or some thing else please try again.")
                print()
                menu()

    def statistics(self):
        print(Color.GREEN + Color.BOLD + "Number of Purchased Tickets: " + Color.END, self.no_of_purchased_tickets)
        per = (self.no_of_purchased_tickets / (rows * cols)) * 100
        print(Color.GREEN + Color.BOLD + "Percentage: " + Color.END, "%.2f" % per, "%")
        print(Color.GREEN + Color.BOLD + "Current income: $" + Color.END, self.current_income)
        print(Color.GREEN + Color.BOLD + "Total Income: $" + Color.END, self.totalIncome)

    def user_info(self):
        row = int(input("Enter the Row Number \n")) - 1
        col = int(input("Enter the Coloum Number \n")) - 1
        print()
        if row >= self.rows or col > self.cols:
            print(Color.RED + Color.BOLD + "There is no such seat in our Theatre." + Color.END)
        elif self.seats[row][col].person is not None:
            print(Color.BOLD + "Name: " + Color.END, self.seats[row][col].person.name)
            print(Color.BOLD + "gender: " + Color.END, self.seats[row][col].person.gender)
            print(Color.BOLD + "age: " + Color.END, self.seats[row][col].person.age)
            print(Color.BOLD + "Ticket Price: $" + Color.END, self.seats[row][col].price)
            print(Color.BOLD + "Phone Number: " + Color.END, self.seats[row][col].person.phone_no)
        else:
            print(Color.BOLD + "Seat is Vacant." + Color.END)


class Person:

    def __init__(self, name, gender, age, phone_no):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_no = phone_no


class Seat:
    def __init__(self, price):
        self.price = price
        self.person = None

    def print_seat(self):
        self.seat


def menu():
    print(Color.BOLD + "1. Show the seats." + Color.END)
    print(Color.BOLD + "2. buy a ticket." + Color.END)
    print(Color.BOLD + "3. statistics." + Color.END)
    print(Color.BOLD + "4. show booked ticket user info." + Color.END)
    print(Color.RED + Color.BOLD + "0. Exit." + Color.END)


# =================================================================================================

rows = int(input("Enter the number of rows: \n"))
cols = int(input("Enter the number of seats in a row: \n"))
print()
menu()
print("=================================")
theatre = Theatre(rows, cols)
option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        print()
        print(Color.BOLD + "Cenima: " + Color.END)
        theatre.print_seats()
        print()
        print(Color.BOLD + "Number of Vacant seats: " + Color.END,
              theatre.vacant_seats - theatre.no_of_purchased_tickets)
        print()
        print(Color.BOLD + "Number of Booked seats: " + Color.END, theatre.no_of_purchased_tickets)
        print("=================================")
        option = int(input("Enter your option: "))
    elif option == 2:
        theatre.book_ticket()
        print("=================================")
        option = int(input("Enter your option: "))
    elif option == 3:
        print()
        theatre.statistics()
        print("=================================")
        option = int(input("Enter your option: "))
    elif option == 4:
        print()
        theatre.user_info()
        print("=================================")
        option = int(input("Enter your option: "))
    elif option != 1 or option != 2 or option != 3 or option != 4 or option != 0:
        print()
        print(Color.RED + Color.BOLD + "Please select the option from the given menu." + Color.END)
        menu()
        print("=================================")
        option = int(input("Enter your option: "))
    if option == 0:
        print()
        print(Color.UNDERLINE + Color.GREEN + Color.BOLD + "Thanks for visiting have a nice day." + Color.END)
        print("=================================")
        break