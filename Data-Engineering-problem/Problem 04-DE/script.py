employees = [
    {"name": "Ali", "department": "IT", "salary": 85000},
    {"name": "Sara", "department": "HR", "salary": 65000},
    {"name": "Ahmed", "department": "IT", "salary": 92000},
    {"name": "Fatima", "department": "Finance", "salary": 78000},
    {"name": "Usman", "department": "HR", "salary": 60000},
    {"name": "Zainab", "department": "IT", "salary": 88000},
    {"name": "Bilal", "department": "Finance", "salary": 95000},
]

def department_summary(raw):
    clean_output = {}
    count = 0
    for record in raw:
     dept = record.get("department","")
     if dept not in clean_output:
          pass
     else:
        clean_output[record.get("department","")] = {"employee_count": count,"total_salary": 0}
output = department_summary(employees)
print(output)