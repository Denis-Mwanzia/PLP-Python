# Function calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        return (100-discount_percent)/100*price
    else:
        return price
    
# Getting User Input
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculating Final Price
final_price = calculate_discount(price, discount_percent)
print(f"Final Price = Ksh. {final_price}.")