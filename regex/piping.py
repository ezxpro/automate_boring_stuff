import re

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group()) # Prints 'Batman'

mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group()) # Prints 'Tina Fey'