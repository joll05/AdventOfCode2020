import re

f=open("input.txt")
Input=f.read().split("\n\n")
f.close()

fieldRegex = r"^(.{3}):(.+)$"
requiredFields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

count = 0
for passport in Input:
    string_fields = passport.split()
    fields = dict([re.match(fieldRegex, f).groups() for f in string_fields])
    if all (f in fields for f in requiredFields):
        count += 1
    
print(count)
