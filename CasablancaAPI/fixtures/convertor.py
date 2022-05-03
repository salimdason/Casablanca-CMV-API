import csv
import json
import time

data = []
with open('01052022.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)

for _ in data[1:]:

    print(_)

    json_bucket =[]

    flights = {
        "model": _[0],
        "fields": {
            "day": _[1],
            "date": _[2],
            "time": _[3],
            "flight": _[4],
            "from": _[5],
            "airline": _[6],
            "aircraft": _[7],
            "status": _[8],
        },

    }

    # print(flights)
    json_bucket.append(flights)

    print(json_bucket)
    # with open('data.json', 'a') as output:
    #     json.dump(json_bucket, output, indent=4, )
    #
    # time.sleep(1)

