import struct
with open('film.data', 'rb') as film_file:
    film = film_file.read()
    name_rus,name_eng,budget,rate,date = struct.unpack('50s50sif10s',film)
    print('{} ({})'.format(name_rus.decode('windows-1251').strip('\x00'),date.decode('windows-1251')[:4]))