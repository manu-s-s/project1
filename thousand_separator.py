import re
def format_number(number):
    number=re.sub(r'(\d{3})(?=\d)',r'\1,',number[::-1])
    return number[::-1]
print(format_number('100000000000'))