import csv

data = []
headers = []

with open("final2.csv", "r") as f:
    csvReader = csv.reader(f)
    for i in csvReader:
        data.append(i)
headers = data[0]
planetData = data[1:]

newData = []

for index, item in enumerate(planetData):
    try:
        if int(item[2]) <= 100 and int(item[9]) > 150 and int(item[9]) < 350:
            newData.append(item)
    except:
        pass

print(len(newData))

with open("filteredData.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(newData)