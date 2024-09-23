
import re
from datetime import datetime
import csv

fileArray = []
dateArr = []
date_data_array = []
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

minimum_len  = min(len(fileArray), len(trueDates))

for n in range(minimum_len):
   date_data_array.append([trueDates[n], fileArray[n]])
   

with open("date_data.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Date", "         HH    DD    FH    FF    FX     T  T10N    TD    SQ     Q    DR    RH     P    VV     N     U    WW    IX     M     R     S     O     Y"])

    for k in date_data_array:
        csv_writer.writerow([k[0].strftime('%Y-%m-%d'), k[1]])  

print(date_data_array)

