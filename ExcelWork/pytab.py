import tablib

headers = ('first_name', 'last_name')

data = [
    ('John', 'Adams'),
    ('George', 'Washington')
]

data = tablib.Dataset(*data, headers=headers)

with open('people.xls', 'wb') as f:
	f.write(data.xls)