# Snack Vending Machine

print("Welcome to the Snack Machine!")
print()

# the snacks, their prices and how many are left
snacks = ["Chips", "Chocolate", "Cookies", "Juice", "Water"]
prices = [3, 4, 2, 5, 1]
stock = [3, 3, 3, 3, 3]

# ask the user how much money they have
money = input("How much money do you have? $")
while not money.isdigit():
    print("Please type a number!")
    money = input("How much money do you have? $")
money = int(money)

total_spent = 0
running = True

while running:
    # show the menu
    print()
    print("------ MENU ------")
    for i in range(len(snacks)):
        print(i + 1, "-", snacks[i], "- $" + str(prices[i]), "- left:", stock[i])
    print("0 - Exit")
    print("Your money: $" + str(money))

    choice = input("What do you want? ")

    if choice == "0":
        running = False
    elif choice.isdigit() and int(choice) <= len(snacks):
        number = int(choice) - 1

        if stock[number] == 0:
            print("Sorry,", snacks[number], "is sold out!")
        elif money < prices[number]:
            print("You don't have enough money for", snacks[number])
        else:
            money = money - prices[number]
            stock[number] = stock[number] - 1
            total_spent = total_spent + prices[number]
            print("You bought", snacks[number] + "! Yum!")
    else:
        print("That is not on the menu!")

    # stop if the user cant afford anything anymore
    if money < min(prices):
        print()
        print("You don't have enough money for anything else.")
        running = False

print()
print("Thank you for visiting!")
print("You spent $" + str(total_spent))
print("You have $" + str(money) + " left")