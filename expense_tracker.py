# Create an empty dictionary to store the expense data
expenses = {}

# Function to add an expense
def add_expense(category, amount, description):
    if category in expenses:
        expenses[category].append((amount, description))
    else:
        expenses[category] = [(amount, description)]
    print("Expense added successfully!")

# Function to view monthly expense summary
def view_summary():
    total_expenses = 0
    for category, items in expenses.items():
        print("Category:", category)
        category_total = 0
        for item in items:
            category_total += item[0]
            print("Amount:", item[0],
        "Description:", item[1],
        "Category Total:", category_total)
        total_expenses += category_total
        print("--------------------")
    print("Total Expenses:", total_expenses)

# Function to handle user interaction
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount spent: "))
            description = input("Enter a brief description: ")
            add_expense(category, amount, description)
        elif choice == "2":
            view_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Start the Expense Tracker
main()