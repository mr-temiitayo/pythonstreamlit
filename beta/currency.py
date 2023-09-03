from forex_python.converter import CurrencyRates

# Initialize the currency converter
c = CurrencyRates()

def currency_converter():
    print("Welcome to Currency Converter!")
    
    while True:
        # Get user input
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ")
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ")
        
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Convert the currency
        converted_amount = c.convert(from_currency, to_currency, amount)
        
        # Display the result
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        
        # Ask if the user wants to convert again
        another_conversion = input("Do you want to convert another amount? (yes/no): ").strip().lower()
        if another_conversion != "yes":
            print("Thank you for using Currency Converter!")
            break

if __name__ == "__main__":
    currency_converter()
