
import re
from datetime import datetime

fileArray = []
dateArr = []
pattern = r"^260,(\d{8})" # regex for YYYYMMDD https://blog.finxter.com/regex-match-dates/ not my code lol, im too stupid for regex


with open("knmi.txt") as file:
    for x in file:
        x = x.strip()
        if (x.startswith("260")):
          
          fileArray.append(x)


for i in range(len(fileArray)):
    match = re.match(pattern, fileArray[i])
    if match:
       date = match.group(1)
       dateArr.append(date)
       fileArray[i] = re.sub(r"^260,\d{8},", "", fileArray[i])

trueDates = [datetime.strptime(date, "%Y%m%d" ) for date in dateArr]

date_data_array = []
minimum_len  = min(len(fileArray), len(trueDates))

for n in range(minimum_len):
   
   date_data_array.append([trueDates[n], fileArray[n]])
   

print(date_data_array)
#print(datarr)

