import csv

file_path = "name+email/name_and_email.csv"

first_name = {}
last_name = {}
email = {}

def parse_data():
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                x=0
                first_name[line_count] = row[0]
                last_name[line_count] = row[1]
                email[line_count] = row[2]
                line_count += 1

def create_and_write_data():
    print_data()

def create_mail():
    pass

def print_data():
    for x in range(len(first_name)):
        print(f'{first_name[x]} {last_name[x]} {email[x]}')

def main():
    parse_data()
    create_and_write_data()

main()