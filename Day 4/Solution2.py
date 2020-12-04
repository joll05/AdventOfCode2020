import re

f=open("input.txt")
Input=f.read().split("\n\n")
f.close()

# Validation functions
def yearValidation(value, Min, Max):
    if(len(value) != 4): return False
    
    try:
        intValue = int(value)
        return Min <= intValue <= Max
    except:
        return False

def byr(value):
    return yearValidation(value, 1920, 2002)

def iyr(value):
    return yearValidation(value, 2010, 2020)

def eyr(value):
    return yearValidation(value, 2020, 2030)

hgtRegex = r"^(\d+)(cm|in)$"
def hgt(value):
    match = re.match(hgtRegex, value)
    if(not match): return False
    lengthValue = int(match.group(1))
    if(match.group(2) == "cm"):
        return 150 <= lengthValue <= 193
    # else
    return 59 <= lengthValue <= 76

hclRegex = r"#[0-9a-f]{6}"
def hcl(value):
    return re.match(hclRegex, value)

def ecl(value):
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def pid(value):
    if(len(value) != 9): return False
    try:
        int(value)
        return True
    except:
        return False
    

fieldRegex = r"^(.{3}):(.+)$"
requiredFields = (("byr", byr), ("iyr", iyr), ("eyr", eyr), ("hgt", hgt), ("hcl", hcl), ("ecl", ecl), ("pid", pid))

count = 0
for passport in Input:
    string_fields = passport.split()
    fields = dict([re.match(fieldRegex, f).groups() for f in string_fields])
    valid = True
    for f in requiredFields:
        if(f[0] not in fields):
            valid = False
            break
        if(not f[1](fields[f[0]])):
            valid = False
            break
    
    if(valid):
        count += 1
    
print(count)
