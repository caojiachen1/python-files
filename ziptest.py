import file
import zipfile
import re
import os

path = file.Get_file()
a = file.zip(path)
a.extractall()
'''
#a = info[0]
print(a.compress_type)
print(a.compress_size)
print(a.original_size)
print(a.last_modified_time)
print(a.compression_rate)'''

