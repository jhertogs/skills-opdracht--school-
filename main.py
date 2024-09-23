
import re
fileArray = []
datarr = []
pattern = r"^260,(\d{8})" # regex for YYYY-MM-DD https://blog.finxter.com/regex-match-dates/ not my code lol, im too stupid for regex


with open("knmi.txt") as file:
    for x in file:
        x = x.strip()
        if (x.startswith("260")):
          
          fileArray.append(x)


for i in range(len(fileArray)):
    match = re.match(pattern, fileArray[i])
    if match:
       date = match.group(1)
       datarr.append(date)
       fileArray[i] = re.sub(r"^260,\d{8},", "", fileArray[i])

#date_objects = [datetime.strptime(date, "%d %b %Y") for date in dates] example im going to plagiarize from myself (earlierr project)

print(fileArray)
#print(datarr)

