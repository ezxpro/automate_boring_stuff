# learn how to match different parts of the expression into separate groups
import re

phone_num_rgx = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_rgx.search('My number is 415-555-4242')

print(mo.group(1))

print(mo.group(2))

print(mo.group(0)) # group 0 returns the full expression returned regex, rather than the parts in parentheses

# to retrieve all groups at once, use groups(), in the plural
print(mo.groups())