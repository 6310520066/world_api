import csv

def get_data_from_csv(filename) -> list:
    with open(filename, "r", encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        return [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]