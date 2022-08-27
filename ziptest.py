import file
import re

path = file.Get_file()
a = file.zip(path)
b = a.fullinfo[0]
b = str(b)
print(b)
b = re.compile(b)
result = b.findall(r"filename='(.*?)'")
print(result)