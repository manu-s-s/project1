import re
urls='''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
urls=pattern.sub(r'\2\3',urls)
print(urls)