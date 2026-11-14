orders = [
    {"order_id": "O001", "product": "Laptop", "quantity": 2, "price": 75000},
    {"order_id": "O002", "product": "Mouse", "quantity": 5, "price": 1200},
    {"order_id": "O003", "product": "Laptop", "quantity": 1, "price": 75000},
    {"order_id": "O004", "product": "Keyboard", "quantity": 3, "price": 2500},
    {"order_id": "O005", "product": "Mouse", "quantity": 2, "price": 1200},
    {"order_id": "O006", "product": "Monitor", "quantity": 1, "price": 18000},
    {"order_id": "O007", "product": "Keyboard", "quantity": 1, "price": 2500},
]
def get_product_summary(raw_data):
    clean_output = {}
    for item in raw_data:
     product = item.get("product","")
    product = item.get("product")
    quantity = item.get("quantity")
    price = item.get("price")
    revenue = quantity * price

    if product in clean_output:
     clean_output[product]["total_quantity"] += quantity
     clean_output[product]["total_revenue"] += revenue
    else: 
     clean_output[product] = {
        "total_quantity": quantity,
        "total_revenue": revenue
    }
    return clean_output
output = get_product_summary(orders)
print(output)