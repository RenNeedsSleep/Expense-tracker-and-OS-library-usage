# Expense-tracker-and-OS-library-usage

This is a simple **command-line program** to track your weekly expenses.
You can add daily expenses, view totals, create or delete categories, and even export your expense table to a file.

---

## 🚀 Features

*  Add expenses for each day of the week.
*  View a **table of expenses** with daily and category totals.
*  See your **weekly totals and averages**.
*  Add new custom categories.
*  Delete unwanted categories.
*  Export your expenses to a `.txt` file for later use.

---

## 📂 File in this project

* **expense_tracker.py** → The main script (contains all the code).

---

## 🖥 Running the Program

1. Make sure you have **Python 3.x** installed.
2. Run the script:

   ```bash
   python expense_tracker.py
   ```
3. Follow the on-screen menu to track your expenses.

---

## 📋 Menu Options

When you run the program, you’ll see this menu:

```
===== WEEKLY EXPENSE TRACKER =====
1. Add an expense
2. View expense table
3. View total expenses
4. Add new category
5. Delete category
6. Export expense table to file
7. Exit
```

---

## ✨ Example Run

```
===== WEEKLY EXPENSE TRACKER =====
1. Add an expense
2. View expense table
3. View total expenses
4. Add new category
5. Delete category
6. Export expense table to file
7. Exit

Enter your choice (1-7): 1

Select a day:
1. Monday
2. Tuesday
...
Enter day number: 1

Select a category:
1. Food
2. Transport
3. Entertainment
4. Utilities
Enter category number: 1
Enter amount for food on monday: $25

Added $25.00 for food on monday.
```

---

## 📦 Exporting

If you choose **option 6**, the program will export your expenses into a neatly formatted text file:

```
expenses.txt
```
which includes the table and summary of totals.
