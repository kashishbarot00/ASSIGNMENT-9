def comptotal(qty, price):
    total = qty * price
    if total > 10000.00:
        total = total * 0.9 
    return total

qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = comptotal(qty, price)

print("Quantity: " ,qty)
print("Price: " ,price)
print("Total: " ,total)
