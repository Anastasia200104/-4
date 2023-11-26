import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def transform() -> None:
    with open(INPUT_FILENAME) as csv_file:
        lines = [line for line in csv.DictReader(csv_file)]

    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(lines, json_file, indent=4)

if name == 'main':
    transform()
    with open(OUTPUT_FILENAME) as output_f:
        for i in output_f:
            print(i, end="")