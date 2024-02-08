import csv

def print_csv_file(file_path):
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        for row in csv_reader:
            print(row)
            row_count += 1
            if row_count >= 1000:
                break
        row_count = 0
        row_count = sum(1 for row in csv_reader)
        print('No of Rows: ',row_count)

# Example usage:
csv_file_path = "D:\dataset.csv"  # Replace 'example.csv' with your CSV file path
print_csv_file(csv_file_path)
