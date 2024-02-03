import csv
import random

def shuffle_csv(input_file, output_file):
    # Read the CSV file into a list of rows
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Shuffle the rows
    random.shuffle(rows)

    # Write the shuffled rows to a new CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Example usage
input_csv = 'Resource-Groups.csv'
output_csv = 'Shuffled-Resource-Groups.csv'

shuffle_csv(input_csv, output_csv)
