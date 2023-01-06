from HW_9.models.loger import CustomManager
import csv
import json


def open_file(name_file):
    with CustomManager(name_file) as file:
        file.read()


def logs_to_csv():
    with open('logs/logs.csv', 'w', newline='') as file_csv:
        writer = csv.writer(file_csv, delimiter=',')
        file_txt = open('logs/logs.txt')
        for line in file_txt:
            words = line.split()
            text_for_csv = [words[0] + ' ' + words[1], ' ' + words[2], ' ' + words[3]]
            writer.writerow(text_for_csv)


def counter_open():
    with open('logs/logs.csv', 'r', newline='') as file_csv:
        reader = csv.reader(file_csv)
        count = 0
        last_time_opened = ''
        for row in reader:
            if ' OPEN' in row:
                count += 1
                last_time_opened = row[0]
        info = {'count': count, 'last_time_opened': last_time_opened}
        info_json = json.dumps({'file.txt': info})
        with open('logs/logs.json', 'w') as file_json:
            file_json.write(info_json)