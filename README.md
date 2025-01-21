Here’s a README file for your program:

---

# Domino's Pizza Order Simulator 🍕

This is a simple Python program that simulates an order system for Domino's Pizza. The user selects their desired pizza size, and optional toppings, and the program calculates the final bill.

## Features
- Choose pizza size: Small (S), Medium (M), or Large (L).
- Add optional toppings:
  - Pepperoni.
  - Extra cheese.
- Calculates the total bill based on selections.

## How It Works
1. The program asks for the user's desired pizza size.
2. It then prompts the user to choose whether to add pepperoni and/or extra cheese.
3. The program calculates the total bill based on the following:
   - **Small Pizza**: $15 
     - Add Pepperoni: +$2
     - Add Extra Cheese: +$1
   - **Medium Pizza**: $20
     - Add Pepperoni: +$3
     - Add Extra Cheese: +$1
   - **Large Pizza**: $25
     - Add Pepperoni: +$3
     - Add Extra Cheese: +$1
4. Finally, the total bill is displayed to the user.

## Prerequisites
- Python 3.x installed on your system.

## How to Run the Program
1. Copy the code into a file named `pizza_order.py`.
2. Open a terminal or command prompt.
3. Run the program with the command:
   ```bash
   python pizza_order.py
   ```
4. Follow the on-screen prompts to place your order.

## Example Interaction
```
Welcome to Domino's Pizza!
What size would you like to have? S, M, L: S
Would you like to have pepperoni? Y or N? Y
Do you want extra cheese? Y or N? Y
Your final bill is $18
```

## Notes
- Ensure to enter valid inputs (S, M, L for size and Y, N for toppings).
- Prices are hardcoded and can be adjusted as needed.

---
