import json
import csv

with open('stations.csv') as file:
     stations =list(csv.DictReader(file))

print(stations)


with open("precipitation.json", encoding='utf-8') as file:
        content = json.load(file)

results = {}
for station in stations:
    all_dates='01 02 03 04 05 06 07 08 09 10 11 12'.split()
    precipi_per_month={}

    for date in all_dates:
        precipi_per_month[date] = 0

    precipi_total=0

    total_precipitation= 0
    print(precipi_per_month)
    for lab in content:
        if lab ['station']==station['Station']:   
            precipi_total += lab['value'] 
            for date in all_dates:
                if lab['date'].startswith(f'2010-{date}'):
                        precipi_per_month[date] += lab['value']

    print(precipi_per_month)

    relative_precipi = {}
    for date in all_dates:
        relative_precipi[date] = precipi_per_month[date]/precipi_total

    print(relative_precipi)
            
    results[station["Location"]]={
         "precipitation_per_month" :precipi_per_month,
         "relative_precipitation":relative_precipi,
         'total_precipitation':precipi_total

    }


with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file,indent=4)



        