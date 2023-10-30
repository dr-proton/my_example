london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london['name'])

london['vendor'] = "cisco"
print(london)

london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}

print(london_co['r1']['model'])

london2 = london.copy()
print(id(london))
print(id(london2))

london["vendor"] = "Juniper"
print(london2)

print(london.get("ios", "Элемента нет"))
london.setdefault("ios", "15.1")
print(london)

print(london.keys())
print(london.values())
print(london.items())
del london["ios"]

print(london)