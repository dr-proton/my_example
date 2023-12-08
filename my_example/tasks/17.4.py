import csv
from datetime import datetime


def write_last_log_to_csv(arg1):
    dct = {}
    with open(arg1, "r", encoding="utf-8") as f1:    
        reader = csv.reader(f1)
        for data in reader:
            if not "Last Changed" in data:
                if dct.get(data[1], None):
                    dct[data[1]].append([data[0], data[-1]])
                else:
                    dct[data[1]] = [[data[0], data[-1]]]

    for k,v in dct.items():
        if len(v) >= 2:
            for i in v:
                print(i[1])

if __name__ == "__main__":
    write_last_log_to_csv("mail_log.csv")