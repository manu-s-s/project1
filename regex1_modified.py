import re
text='''b
a
u.C0
12
cat
mat
pat
bat
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T'''
pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches=pattern.finditer(text)
for match in matches:
    print(match)