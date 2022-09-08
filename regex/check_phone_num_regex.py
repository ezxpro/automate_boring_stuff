import re

def isPhoneNumber(text):
    regexObject =  re.compile(r'\d{3}-\d{3}-\d{4}') 
    matchObject = regexObject.search(text)
    if matchObject == None:
        return False
    else:
        return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi '))