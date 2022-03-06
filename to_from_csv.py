import csv

def csv_reader(file):
    with open(f'{file}') as f:
        fieldnames = ['name', 'symbol', 'price']
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in csv_reader:
            print(row)


def main():
    csv_reader('crypto.csv')

if __name__ == '__main__':
    main()