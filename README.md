# currency_converter

I'll walk you through building the currency converter step by step, explaining each concept along the way so you can understand the syntax and how it all works.

Let's break it down:

### Step 1: Setting Up the Basic Structure

A currency converter needs the following components:
1. A way to input the amount to convert.
2. A way to choose the currency you want to convert from and to.
3. A way to get the conversion rate (we’ll use a static rate for simplicity).
4. A way to display the result.

Let’s start by setting up a basic structure of the app.

```python
def currency_converter():
    print("Welcome to the Currency Converter!")

    # Step 2: Get input from the user
    amount = float(input("Enter the amount you want to convert: "))
    print(f"You are converting {amount}")

    from_currency = input("Enter the currency you are converting from (e.g., USD): ")
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ")

    # Step 3: Set up conversion rates
    conversion_rate = 0.85  # Example conversion rate (USD to EUR)

    # Step 4: Perform the conversion
    converted_amount = amount * conversion_rate

    # Step 5: Display the result
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

# Call the function to run the program
currency_converter()
```

### Explanation:

- **`def currency_converter():`**
  - This is the function definition. `def` is used to define a function. Functions help in organizing the code and reusing it.
  
- **`input()`**
  - This is a built-in Python function to get input from the user. It always returns the input as a string, so we convert it into a float using `float()`.
  
- **String formatting: `f"{variable}"`**
  - This is an f-string, a more modern and clean way to embed variables directly into strings.

- **Variables**
  - `amount`, `from_currency`, `to_currency` are all variables that store user inputs.
  
- **Basic Arithmetic**
  - We perform a simple multiplication to convert the amount based on the `conversion_rate`.

### Step 2: Enhancing the Conversion Rate (Optional)

Right now, the conversion rate is hard-coded, but in a real-world application, you would probably want to fetch the current conversion rates from an API. For simplicity, let's continue with static values, but later I can show you how to fetch rates from a service like `ExchangeRate-API` if you want.

### Step 3: Adding Multiple Conversion Rates

Now, let’s make it a bit more flexible by adding multiple currencies and conversion rates.

```python
def currency_converter():
    print("Welcome to the Currency Converter!")

    # Step 2: Get input from the user
    amount = float(input("Enter the amount you want to convert: "))
    print(f"You are converting {amount}")

    from_currency = input("Enter the currency you are converting from (e.g., USD): ")
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ")

    # Step 3: Set up conversion rates
    conversion_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75, "INR": 74.5},
        "EUR": {"USD": 1.18, "GBP": 0.88, "INR": 88.0},
        "GBP": {"USD": 1.33, "EUR": 1.14, "INR": 100.5},
        "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.0099}
    }

    # Step 4: Perform the conversion based on the user's choice
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        conversion_rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Sorry, we don't support this conversion.")

# Call the function to run the program
currency_converter()
```

### Explanation of Changes:
- **Dictionary (`conversion_rates`)**
  - We now store conversion rates in a dictionary. This is a way of organizing data in Python. Dictionaries are key-value pairs (`key: value`). 
  - We nested dictionaries to store multiple rates for each currency.
  
- **Conditional Check**
  - We use an `if` condition to check if the user’s inputted currencies exist in the dictionary. If they do, we fetch the conversion rate; if not, we print a message saying the conversion is unsupported.

### Step 4: Error Handling (User Input)

Sometimes users will input incorrect data. We can handle that by adding error handling.

```python
def currency_converter():
    print("Welcome to the Currency Converter!")

    try:
        # Step 2: Get input from the user
        amount = float(input("Enter the amount you want to convert: "))
        print(f"You are converting {amount}")

        from_currency = input("Enter the currency you are converting from (e.g., USD): ")
        to_currency = input("Enter the currency you are converting to (e.g., EUR): ")

        # Step 3: Set up conversion rates
        conversion_rates = {
            "USD": {"EUR": 0.85, "GBP": 0.75, "INR": 74.5},
            "EUR": {"USD": 1.18, "GBP": 0.88, "INR": 88.0},
            "GBP": {"USD": 1.33, "EUR": 1.14, "INR": 100.5},
            "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.0099}
        }

        # Step 4: Perform the conversion based on the user's choice
        if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
            conversion_rate = conversion_rates[from_currency][to_currency]
            converted_amount = amount * conversion_rate
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Sorry, we don't support this conversion.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")

# Call the function to run the program
currency_converter()
```

### Explanation of Error Handling:
- **`try` and `except` Block**
  - This is a basic form of error handling in Python. The `try` block will execute the code, and if an error occurs (like the user entering something that can’t be converted to a float), it will jump to the `except` block and display a friendly error message.

### Final Thoughts:
- We’ve covered basic syntax (functions, conditionals, loops), dictionaries, and error handling.
- You can improve this by fetching real-time conversion rates from an API like `ExchangeRate-API` for more accuracy.
