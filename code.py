import tkinter as tk
from tkinter import messagebox

# List to store expenses
expenses = []


# Function to add expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()

    if date == "" or category == "" or description == "" or amount == "":
        messagebox.showwarning("Warning", "Please fill all the details")
    else:
        amount = float(amount)

        expense = [date, category, description, amount]
        expenses.append(expense)

        messagebox.showinfo("Success", "Expense added successfully")

        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)


# Function to show expenses
def show_expenses():
    if len(expenses) == 0:
        messagebox.showinfo("Expenses", "No expenses added")
    else:
        result = ""

        for i in range(len(expenses)):
            result = result + str(i + 1) + ". "
            result = result + "Date: " + expenses[i][0] + ", "
            result = result + "Category: " + expenses[i][1] + ", "
            result = result + "Description: " + expenses[i][2] + ", "
            result = result + "Amount: ₹" + str(expenses[i][3]) + "\n"

        messagebox.showinfo("All Expenses", result)


# Function to delete an expense
def delete_expense():
    number = delete_entry.get()

    if number == "":
        messagebox.showwarning("Warning", "Enter expense number")
    else:
        number = int(number)

        if number > 0 and number <= len(expenses):
            expenses.pop(number - 1)

            messagebox.showinfo("Success", "Expense deleted")

            delete_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Invalid expense number")


# Function to calculate total expense
def total_expense():
    total = 0

    for i in range(len(expenses)):
        total = total + expenses[i][3]

    messagebox.showinfo("Total Expense", "Total Expense = ₹" + str(total))


# Function to clear all expenses
def clear_all():
    expenses.clear()

    messagebox.showinfo("Success", "All expenses deleted")


# Create main window
window = tk.Tk()
window.title("Smart Student Expense Tracker")
window.geometry("500x600")


# Heading
title = tk.Label(window,text="Smart Student Expense Tracker",font=("Arial", 18, "bold"))
title.pack(pady=20)


# Date
tk.Label(window, text="Date").pack()
date_entry = tk.Entry(window)
date_entry.pack()


# Category
tk.Label(window, text="Category").pack()
category_entry = tk.Entry(window)
category_entry.pack()


# Description
tk.Label(window, text="Description").pack()
description_entry = tk.Entry(window)
description_entry.pack()


# Amount
tk.Label(window, text="Amount").pack()
amount_entry = tk.Entry(window)
amount_entry.pack()


# Add button
add_button = tk.Button(window,text="Add Expense",command=add_expense)
add_button.pack(pady=10)


# Show button
show_button = tk.Button(window,text="Show Expenses",command=show_expenses)
show_button.pack(pady=5)


# Total button
total_button = tk.Button(window,text="Total Expense",command=total_expense)
total_button.pack(pady=5)


# Delete section
tk.Label(window, text="Enter Expense Number to Delete").pack(pady=10)

delete_entry = tk.Entry(window)
delete_entry.pack()

delete_button = tk.Button(window,text="Delete Expense",command=delete_expense)
delete_button.pack(pady=5)


# Clear all button
clear_button = tk.Button(window,text="Clear All Expenses",command=clear_all)
clear_button.pack(pady=10)


# Start the program
window.mainloop()

