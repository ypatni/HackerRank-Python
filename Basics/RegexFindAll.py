import re
x = input()
vowels = 'aeiouAEIOU'
consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM '
ans = re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(consonants,vowels,consonants),x)
print('\n'.join(ans or -1))
