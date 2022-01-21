from shop.orders import create_new_order

print("Witaj w naszym sklepie")
product_name = input("Jaki towar chcesz kupić: ")
quantity = int(input("ile sztuk/kg chcesz kupić: "))


result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"łączny koszt wynosi {total_price} zł")
