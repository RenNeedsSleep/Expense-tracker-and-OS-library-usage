categories = ['food', 'transport', 'entertainment', 'utilities']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

expenses = {}
for day in days:
    expenses[day] = {}
    for category in categories:
        expenses[day][category] = 0

def show_menu():
    """Display the main menu options"""
    print("\n===== WEEKLY EXPENSE TRACKER =====")
    print("1. Add an expense")
    print("2. View expense table")
    print("3. View total expenses")
    print("4. Add new category")
    print("5. Delete category")
    print("6. Export expense table to file")
    print("7. Exit")

def add_expense():

    print("\nSelect a day:")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day.capitalize()}")

    try:
        day_index = int(input("Enter day number: ")) - 1
        if day_index < 0 or day_index >= len(days):
            print("Invalid day number.")
            return
        selected_day = days[day_index]
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nSelect a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")

    try:
        category_index = int(input("Enter category number: ")) - 1
        if category_index < 0 or category_index >= len(categories):
            print("Invalid category number.")
            return
        selected_category = categories[category_index]
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        amount = float(input(f"Enter amount for {selected_category} on {selected_day}: $"))
        if amount < 0:
            print("Amount cannot be negative.")
            return

        expenses[selected_day][selected_category] = amount
        print(f"Added ${amount:.2f} for {selected_category} on {selected_day}.")
    except ValueError:
        print("Please enter a valid amount.")

def display_table():

    header = "           |"
    for category in categories:
        header += f" {category[:7]:7} |"
    header += " Daily Tot |"
    print(header)

    separator = "-----------+"
    for _ in range(len(categories) + 1): 
        separator += "----------+"
    print(separator)
    
    for day in days:
        daily_total = sum(expenses[day].values())
        row = f"{day[:10]:10} |"
        for category in categories:
            amount = expenses[day][category]
            row += f" ${amount:7.2f} |"
        row += f" ${daily_total:7.2f} |"
        print(row)
    
    print(separator)

    row = "Category Tot|"
    for category in categories:
        category_total = sum(expenses[day][category] for day in days)
        row += f" ${category_total:7.2f} |"

    weekly_total = sum(sum(expenses[day].values()) for day in days)
    row += f" ${weekly_total:7.2f} |"
    print(row)

def view_total():

    total = 0
    for day in days:
        for category in categories:
            total += expenses[day][category]
    
    print(f"\nTotal expenses for the week: ${total:.2f}")

    print("\nDaily averages:")
    for day in days:
        day_total = sum(expenses[day].values())
        print(f"  {day.capitalize()}: ${day_total:.2f}")
    
    print("\nCategory totals:")
    for category in categories:
        category_total = sum(expenses[day][category] for day in days)
        daily_avg = category_total / len(days)
        print(f"  {category.capitalize()}: ${category_total:.2f} (avg ${daily_avg:.2f}/day)")

def add_category():
    
    new_category = input("\nEnter new category name: ").lower().strip()
    
    if not new_category:
        print("Category name cannot be empty.")
        return
        
    if new_category in categories:
        print(f"Category '{new_category}' already exists.")
        return

    categories.append(new_category)
    
    for day in days:
        expenses[day][new_category] = 0
    
    print(f"Added new category: {new_category}")

def delete_category():

    print("\nSelect a category to delete:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")
    
    
    try:
        category_index = int(input("Enter category number: ")) - 1
        if category_index < 0 or category_index >= len(categories):
            print("Invalid category number.")
            return
        selected_category = categories[category_index]
    except ValueError:
        print("Please enter a valid number.")
        return
    
    
    confirm = input(f"Are you sure you want to delete '{selected_category}'? (y/n): ").lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return
    
    
    for day in days:
        del expenses[day][selected_category]
    
    
    categories.remove(selected_category)
    print(f"Category '{selected_category}' deleted.")

def export_to_file():
    """Export expense table to a text file"""
    filename = input("\nEnter filename (default: expenses.txt): ").strip()
    if not filename:
        filename = "expenses.txt"
    
    # Add .txt extension if not provided
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            # Write header
            header = "           |"
            for category in categories:
                header += f" {category[:7]:7} |"
            header += " Daily Tot |"
            file.write(header + "\n")

            # Write separator
            separator = "-----------+"
            for _ in range(len(categories) + 1): 
                separator += "----------+"
            file.write(separator + "\n")
            
            # Write daily expenses
            for day in days:
                daily_total = sum(expenses[day].values())
                row = f"{day[:10]:10} |"
                for category in categories:
                    amount = expenses[day][category]
                    row += f" ${amount:7.2f} |"
                row += f" ${daily_total:7.2f} |"
                file.write(row + "\n")
            
            # Write separator
            file.write(separator + "\n")

            # Write category totals
            row = "Category Tot|"
            for category in categories:
                category_total = sum(expenses[day][category] for day in days)
                row += f" ${category_total:7.2f} |"

            weekly_total = sum(sum(expenses[day].values()) for day in days)
            row += f" ${weekly_total:7.2f} |"
            file.write(row + "\n")
            
            # Write summary section
            file.write("\n\nSUMMARY\n")
            file.write("========\n")
            file.write(f"Total expenses for the week: ${weekly_total:.2f}\n\n")
            
            file.write("Daily totals:\n")
            for day in days:
                day_total = sum(expenses[day].values())
                file.write(f"  {day.capitalize()}: ${day_total:.2f}\n")
            
            file.write("\nCategory totals:\n")
            for category in categories:
                category_total = sum(expenses[day][category] for day in days)
                daily_avg = category_total / len(days)
                file.write(f"  {category.capitalize()}: ${category_total:.2f} (avg ${daily_avg:.2f}/day)\n")
                
        print(f"\nExpense table exported to '{filename}' successfully!")
    except IOError:
        print(f"\nError: Unable to write to file '{filename}'")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            display_table()
        elif choice == '3':
            view_total()
        elif choice == '4':
            add_category()
        elif choice == '5':
            delete_category()
        elif choice == '6':
            export_to_file()
        elif choice == '7':
            print("\nThank you for using the Weekly Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()