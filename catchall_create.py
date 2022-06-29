import csv
import random

domain = "theorangecomp.com"

file_path_read = "name+email/name_and_email.csv"
file_path_write = "name+email/new_name_and_email.csv"

first_name = {}
last_name = {}
email = {}

header = ["first_name", "second_name", "email"]


def parse_data():
    with open(file_path_read) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                x = 0
                first_name[line_count] = row[0]
                last_name[line_count] = row[1]
                email[line_count] = row[2]
                line_count += 1


def create_and_write_data():
    # print_data()
    with open(file_path_write, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for x in range(1, len(first_name) + 1):
            writer.writerow(create_mail(x))


def create_mail(x):
    rand_num = random.randint(1, 99)
    return [
        first_name[x],
        last_name[x],
        f"{first_name[x]}.{last_name[x]}{rand_num}@{domain}",  # catchall mail
    ]


def print_data():
    for x in range(1, len(first_name) + 1):
        print(f"{first_name[x]} {last_name[x]} {email[x]}")


def main():
    parse_data()
    create_and_write_data()


main()
