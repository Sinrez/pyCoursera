import sys
import struct
def detect():
    file = sys.argv[1]
    with open(file,'rb') as image_file:
        image = struct.unpack('3s',image_file.read(3))
        if image[0] == b'\xff\xd8\xff':
            print('jpeg')

        elif image[0] == b'\x89PN':
            print('png')

        elif image[0] == b'GIF':
            print('gif')
        else:
            print('None')
detect()