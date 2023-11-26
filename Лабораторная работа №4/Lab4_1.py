# TODO решите задачу
import json
def task() -> float:
    file = "input.json"
    with open(file) as f:
        json_data = json.load(f)

    summa = sum([item["score"] * item["weight"] for item in json_data])
    return round(summa, 3)

print(task())