import csv

with open('f4.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Si hay encabezados, omítelos
        for row in csv_reader:
            print(row[5])