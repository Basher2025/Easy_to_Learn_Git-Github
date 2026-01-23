import csv
from importlib.resources import path


def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
    # This change is to return the rows after reading from the CSV file
    return rows
