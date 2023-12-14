import csv
import random

# Reading the CSV file
with open('data/populations.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Function to get a random row and another row within 10 positions but not the same
def get_random_rows():
    random_row = random.choice(data)
    index = data.index(random_row)
    
    # Keep selecting a different row until it's different from the first one
    while True:
        second_row_index = random.randint(max(0, index - 10), min(len(data) - 1, index + 10))
        second_row = data[second_row_index]
        if second_row != random_row:
            return (tuple(random_row.items()), tuple(second_row.items()))


def main():
    result = get_random_rows()
    print(result)


if __name__ == '__main__':
    main()