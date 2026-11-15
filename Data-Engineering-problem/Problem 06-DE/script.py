users: list[dict[str, str]] = [
    {"name": "  ayan  ", "email": "AYAN@EXAMPLE.COM", "city": "gilgit"},
    {"name": "ALI", "email": "  ali@example.com  ", "city": "LAHORE"},
    {"name": "  Sara ", "email": "SARA@EXAMPLE.COM", "city": "  karachi"},
]

def clean_user_data(users: list[dict[str, str]]) -> list[dict[str, str]]:
    clean_output = []
    for record in users:
        clean_output.append({
            "name": record.get("name","").strip().title(),
            "email": record.get("email","").strip().lower(),
            "city": record.get("city","").strip().title(),
        })
    return clean_output
print(clean_user_data(users))
