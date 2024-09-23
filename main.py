
import re
fileArray = []
pattern = "^260,\d{4}-\d{2}-\d{2}$" # regex for YYYY-MM-DD https://blog.finxter.com/regex-match-dates/ not my code lol, im too stupid for regex


with open("knmi.txt") as file:
    for x in file:
        x = x.strip()
        if (x.startswith("260")):
          fileArray.append(x)


   



print(fileArray)
