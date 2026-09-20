import email
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


cat
mat
pat
bat
hat
'''

emails = """
RohitSRasam@gmail.com
rohit.rasam@university.edu
rohit-321-rasam@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

sentence = 'Start a sentence and bring it to an end'

# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')   # find all the numbers
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')   # find numbers with dash or dots in them
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')   # find all 800 or 900 numbers
# pattern = re.compile(r'[1-5]')   # find numbers between 1 to 5
# pattern = re.compile(r'[^a-zA-Z]')  # carret inside the character set finds everything that is not in the character set
# pattern = re.compile(r'[^b]at') # find all the words not starting with `b`
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')   # find all the numbers using quantifiers
# pattern = re.compile(r'Mr\.?\s?[A-Z]\w*')   # finds names starting with `Mr`
# pattern = re.compile(r'M(r|s|rs)\.?\s?[A-Z]\w*')   # finds names starting with `Mr`, `Mrs`, `Ms`
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s?[A-Z]\w*')   # finds names starting with `Mr`, `Mrs`, `Ms`
# pattern = re.compile(r'[A-Za-z.0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # find urls
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)
# matches = pattern.finditer(urls)
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')

# matches = pattern.finditer(sentence)
# matches = pattern.findall(urls)   # return matches as a list of string

pattern = re.compile(r'Start')
matches = pattern.match(sentence)   # matches only the beginning of the string

# for match in matches:
    # print(f'{match.group(0)} = {match.group(1)} + {match.group(2)} + {match.group(3)}')
print(matches)
