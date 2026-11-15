amounts: list[float] = [100.50, -50.0, 200.0, 0.0, 75.25, -10.0]

def filter_positive_amounts(amounts: list[float]) -> list[float]:
    
    clean_ouput = [amount for amount in amounts if amount > 0]
    return clean_ouput
print(filter_positive_amounts(amounts))