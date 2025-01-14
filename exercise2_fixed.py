import json

with open("precipitation.json", encoding='utf-8') as file:
        content = json.load(file)



all_dates='01 02 03 04 05 06 07 08 09 10 11 12'.split()
precipi_per_month={}
percentage_particiation={}

for date in all_dates:
      precipi_per_month[date] = 0
total_precipi=0

total_precipitation= 0
print(precipi_per_month)
for lab in content:
     if lab ['station']=='GHCND:US1WAKG0038':   
          total_precipi += lab['value'] 
          for date in all_dates:
               if lab['date'].startswith(f'2010-{date}'):
                    precipi_per_month[date] += lab['value']

print(precipi_per_month)


for date in all_dates:
     percentage_particiation[date] = precipi_per_month[date]/total_precipi

Seattle={
     'precipitation_per_month' :precipi_per_month,
     'percentage_precipitation':percentage_particiation,
     'total_precipitaiton':total_precipi,
}
print(Seattle)
        



with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Seattle, file,indent=4)
