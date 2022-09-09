import re

phone_num_rgx = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_rgx.search('My number is 415-555-4242')

print(mo.group(1))

print(mo.group(2))

print(mo.group(0))