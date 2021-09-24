import re
text1='''hel   lmmoo
ooooing
hel   lmmoo
ooooing'''
text='''bal
a
u C0
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
pattern=re.compile(r'''^hel  \sl.+o*
o*ing$''',re.M)
matches=pattern.finditer(text1)
for match in matches:
    print(match)