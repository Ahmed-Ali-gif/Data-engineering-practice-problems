students = [
    {"name": "Ali", "marks": [78, 85, 90]},
    {"name": "Sara", "marks": [92, 88, 95]},
    {"name": "Ahmed", "marks": [45, 50, 40]},
    {"name": "Fatima", "marks": [70, 65, 80]},
    {"name": "Usman", "marks": [30, 25, 35]},
]

def get_top_students(raw_data):
    clean_output = []
    for record in raw_data:
        total = sum(record.get("marks",0))
        count = len(record.get("marks",0))
        avg_marks = total / count
        if avg_marks >= 70:
           dict_output={
             "name": record.get("name",""),
             "average": round(avg_marks,2)
           }
           clean_output.append(dict_output)
    clean_output.sort(key=lambda x: x["average"], reverse=True)
    return clean_output
x = get_top_students(students)
print(x)
