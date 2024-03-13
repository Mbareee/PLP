def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        print(f'${price - (price*discount_percent/100)}')
        
    else:
        print(f'${price}')

price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount of the item: "))
calculate_discount(price, discount_percent)