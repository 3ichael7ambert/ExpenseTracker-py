# Expense Tracker Program

# Initialize empty dictionaries to store expenses and category totals
expenses = {}
category_totals = {}


# Function to get user input for expenses
def get_user_input():
  user_input = input(
      "Enter expense (format: category name comma amount,(EX: 'food, 10') type 'exit' to finish): "
  )
  return user_input


# Function to validate user input
def is_valid_input(user_input):
  # Validate that user_input is not 'exit'
  if user_input.lower() == 'exit':
    return True
  # Validate the format of the input (e.g., 'category amount')
  elif len(user_input.split()) != 2:
    print(
        "Invalid input format. Please use 'category amount' or type 'exit' to finish."
    )
    return False
  # Additional validation logic can be added as needed
  else:
    return True


# Function to parse user input into category and amount
def parse_input(user_input):
  category, amount = user_input.split()
  return category, float(amount)


# Function to update expenses dictionary
def update_expenses(expenses, category, amount):
  if category in expenses:
    expenses[category].append(amount)
  else:
    expenses[category] = [amount]


# Function to update category totals dictionary
def update_category_totals(category_totals, category, amount):
  if category in category_totals:
    category_totals[category] += amount
  else:
    category_totals[category] = amount


# Function to display final expense summary
def display_summary(expenses, category_totals):
  print("\nExpense Summary:")
  for category, total in category_totals.items():
    print(f"{category.capitalize()}: ${total:.2f}")
  print("Individual Expenses:")
  for category, items in expenses.items():
    print(f"{category.capitalize()}: {', '.join(map(str, items))}")


# Main program loop
user_input = ""
# Main program loop
while True:
  user_input = get_user_input()

  # Validate input and process expenses
  if user_input.lower() == 'exit':
    break  # Exit the loop if the user types 'exit'

  if is_valid_input(user_input):
    try:
      category, amount = parse_input(user_input)
      update_expenses(expenses, category, amount)
      update_category_totals(category_totals, category, amount)
    except ValueError as e:
      print(
          f"Error: {e}. Please use 'category [string] then comma then  amount' (EX: 'food, 10') or type 'exit' to finish."
      )
  else:
    print(
        "Invalid input format. Please use 'category amount' or type 'exit' to finish."
    )

# Display final expense summary
display_summary(expenses, category_totals)
