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
