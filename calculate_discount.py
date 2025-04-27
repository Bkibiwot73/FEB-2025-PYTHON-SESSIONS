# Define the function to calculate discount
def calculate_discount(price, discount_percent): 
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate how much the discount is
        final_price = price - discount_amount  # Subtract the discount from the original price
        return final_price  # Return the final price after discount
    else:
        return price  # If discount is less than 20%, return the original price

# Test the function manually with example values
print(calculate_discount(100, 25))  # Should print 75.0 because 25% discount is applied

# Ask the user for the original price and discount
try:
    price = float(input("Enter the original price of the item: "))  # Get price from user
    discount_percent = float(input("Enter the discount percentage: "))  # Get discount percentage from user

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the result to the user
    print(f"The final price is: ${final_price:.2f}")

except ValueError:
    # Handle wrong input (like letters instead of numbers)
    print("Please enter valid numbers for price and discount.")
