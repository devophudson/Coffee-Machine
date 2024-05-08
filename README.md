## Description:

This Python code implements a basic simulator of a coffee machine. The machine offers three types of drinks: espresso, latte, and cappuccino. Each drink has its own recipe of ingredients and associated cost.

The code keeps track of the available resources in the machine, such as water, milk, and coffee, as well as tracking the total cost of sales made.

The main components of the code are:

MENU: A dictionary defining the available drink options, along with the required ingredients and costs associated with each.

resources: A dictionary tracking the available quantity of each resource in the machine.

Functions:

check_resources: Checks if there are sufficient resources in the machine to make the requested drink.
process_payment: Prompts the user to input the payment amount and calculates the total received.
transaction_success: Checks if the payment is sufficient and provides change if necessary.
make_coffee: Deducts the ingredients used to make the drink from the total available resources.
Main loop: Executes the main program, where the user can choose a drink, check the resource report, or power off the machine.

This code can be useful for understanding the basic principles of transaction processing, resource control, and data structures in Python, as well as serving as a foundation for developing more complex beverage sales management systems.
