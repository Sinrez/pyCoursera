import re
# result = re.match('You', 'Young Frankenstein')
# print(result)


source = 'Young Frankenstein'
if m := re.search('Frank', source):
         print(m.group())

