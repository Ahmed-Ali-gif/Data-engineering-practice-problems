transactions = [
    {"customer_id": "C001", "amount": 150.0, "status": "completed"},
    {"customer_id": "C002", "amount": 80.5, "status": "pending"},
    {"customer_id": "C001", "amount": 45.0, "status": "completed"},
    {"customer_id": "C003", "amount": 200.0, "status": "failed"},
    {"customer_id": "C002", "amount": 120.0, "status": "completed"},
    {"customer_id": "C001", "amount": 30.0, "status": "pending"},
]
# rules total amount calculate , filter the customers thats are not completed
def process_transactions(raw):
 clean_output = {}
 for record in raw:
    if record.get("status") == "completed":
      customer = record.get("customer_id")
      amount = record.get("amount")
      clean_output[customer] = clean_output.get(customer,0) + amount
 return clean_output

output = process_transactions(transactions)
print(output)