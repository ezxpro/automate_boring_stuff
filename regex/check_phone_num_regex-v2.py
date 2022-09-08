import re

def isPhoneNumber(text):
    regexObject =  re.compile(r'\d{3}-\d{3}-\d{4}') 
    matchObject = regexObject.search(text)
    if matchObject == None:
        return False
    else:
        return True

def retRegexMatch(text):
    regexObject = re.compile(r'\d{3}-\d{3}-\d{4}') 
    matchObject = regexObject.search(text)
    if matchObject == None:
        return None
    else:
        return matchObject.group()

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
match = retRegexMatch(message)
print(match)
'''
for i in match if match != None:
    print({Phone number found: i)
'''
