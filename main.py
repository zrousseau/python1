import os
import platform
import re

if __name__ == '__main__':
    import random

    print(platform.uname())
    # os.uname is apparently only works on UNIX systems? I guess platform.uname acheives a similar affect
    print(re.search('sys.+dows\'', str(platform.uname())))

    if os.access("testfile.txt", os.R_OK):
        file = open("testfile.txt", 'r')
        print(re.findall('c[a-zA-z]+', file.read()))

    list = re.split('er$', os.getlogin())
    print(list)

    # sorry if this is not fantastic first time using regex
    # it was a friday afternoon when I started and I didn't know if you would respond so I decided to see how i could do