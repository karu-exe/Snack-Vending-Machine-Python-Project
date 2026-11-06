# Snack Vending Machine Python Project
A terminal based vending machine simulator in Python that manages a menu, stock and a user’s balance using lists, loops and conditionals.


A Python program that simulates a snack vending machine in the terminal. The user enters how much money they have, then buys snacks from a numbered menu until they choose to exit or can’t afford anything else. The program tracks the user’s remaining money, the stock of each snack and the total amount spent.

Features

Displays a menu with each snack’s name, price and remaining stock
Lets the user buy multiple snacks in one session
Shows a “sold out” message when a snack runs out
Warns the user when they don’t have enough money for an item
Handles invalid input, such as letters instead of numbers or menu choices that don’t exist
Ends automatically when the user can’t afford any more snacks
Prints a summary of total money spent and money left at the end

Concepts used

Variables and user input with input()
Lists, including parallel lists for snack names, prices and stock
for and while loops
Conditional statements (if, elif, else)
Basic input validation with .isdigit()
Simple arithmetic to update money and stock
