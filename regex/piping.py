import re

hero_regex = re.compile(r'Batman|Tina Fey')
mo = hero_regex.search('Batman and Tina Fey')
print(mo.group()) # Prints 'Batman'

mo = hero_regex.search('Tina Fey and Batman')
print(mo.group()) # Prints 'Tina Fey'

# Specify a prefix to be searched by the regex
print("Let's go for the second part now")
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')

print(mo.group())
print(mo.group(1))