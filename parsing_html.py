import csv

html_output = ''
names = []

with open('patreons.csv','r') as data_files:
    csv_data = csv.DictReader(data_files)




    # we dont want headers or first line bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

# for name in names:
#     print(name)
