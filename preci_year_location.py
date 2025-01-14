import json

with open("precipitation.json", encoding='utf-8') as file:
        content = json.load(file)



dictio_seattle={}


all_location= 'GHCND:USW00093814 GHCND:US1WAKG0038 GHCND:USC00513317 GHCND:US1CASD0032'.split()
precipi_per_location={}
for location in all_location:
      precipi_per_location[location] = 0


for lab in content:
     for location in all_location:
        if lab['station'] == location:
              precipi_per_location[location] += lab['value']

print(precipi_per_location)
          
"""with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipi_per_location, file,indent=4)
          """