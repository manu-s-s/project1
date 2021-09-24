import re
text='''
hahahaha'''

print(re.findall('(?=aha)',text))
print(len(re.findall('(?=aha)',text)))