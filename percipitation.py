import json

with open("precipitation.json", encoding='utf-8') as file:
        content = json.load(file)



dictio_seattle={}


all_dates='01 02 03 04 05 06 07 08 09 10 11 12'.split()
precipi_per_month={}
for date in all_dates:
      precipi_per_month[date] = 0

print(precipi_per_month)

for lab in content:
     if lab ['station']=='GHCND:US1WAKG0038':
          for date in all_dates:
               if lab['date'].startswith(f'2010-{date}'):
                    precipi_per_month[date] += lab['value']


print(f' for {date} precipitation is {precipi_per_month}')
          
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipi_per_month, file,indent=4)
          



        