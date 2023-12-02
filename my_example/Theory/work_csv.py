import csv

with open("sw_data.csv", "r", encoding="utf-8") as file:
    data = csv.reader(file)
    for i in data:
        print(i)

print("=" * 100)

with open("sw_data.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file))
    print(data)

print("=" * 100)

with open("sw_data.csv", "r", encoding="utf-8") as file:
    data = csv.reader(file)
    headers = next(data)
    print("Headers: ", headers)
    for row in data:
        print(row)

print("=" * 100)

with open("sw_data.csv", "r", encoding="utf-8") as file:
    data = csv.DictReader(file)
    for i in data:
        print(i)
        print(i['hostname'], i['model'])

print("=" * 100)

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open("write_csv.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     for i in data:
#         writer.writerow(i)

print("=" * 100)

# with open("write_csv.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(data)


data2 = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open("write_csv.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=list(data2[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data2:
        writer.writerow(d)