import validators
# if validators.url("https://elar.urfu.ru/bitstream/10995/28769/1/978-5-7996-1198-9_2014.pdf"):
if validators.url("abc"):
    print('valid')
else:
    print('not')

