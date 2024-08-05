import re

test_ids = ["ABC1234", "sbaz56", "Wuy1452", "TYP9006", "KZED439"]
pattern = '^[A-Z]{3}\d{4}$'
valid_ids = []

for ids in test_ids:
    if re.fullmatch(pattern,ids):
        valid_ids.append(ids)
print('Valid IDs=',valid_ids)

'''
^ means the starting of a string
$ means the ending of a string
[A-Z]{3} means 3 chars from A - Z
\d{4} means 4 digits

'''