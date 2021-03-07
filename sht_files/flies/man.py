import struct
name = 'Альберт'
lname = 'Эйнштейн'
birthday = 1879
death = 1955

with open('scientist.bin', 'wb') as scientist_file:
    scientist_name = struct.pack('50s', name.encode())
    scientist_lname = struct.pack('50s', lname.encode())
    scientist_birthday = struct.pack('h',birthday)
    scientist_death = struct.pack('h', death)

    scientist_file.write(scientist_name)
    scientist_file.write(scientist_lname)
    scientist_file.write(scientist_birthday)
    scientist_file.write(scientist_death)
