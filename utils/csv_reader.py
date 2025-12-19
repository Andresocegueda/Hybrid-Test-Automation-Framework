import csv

def get_csv_data(file_name):
    rows = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            row[2] = row[2] == 'True'
            rows.append(row)
    return rows