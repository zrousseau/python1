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
