import zipfile
import os

folder = 'src\\'

files = os.listdir(folder)
res_f = {}
res_s = []
res_t = []

for file in files:
    try:
        info = (zipfile.ZipFile('channel.zip').getinfo(file).comment).decode('utf-8')
        res_f.update({file : info})
    except KeyError:
        pass

fileName = '90052.txt'

while True:
    try:
        line = open(folder + fileName).read()

        nextName = int(line[16:])
        fileName = str(nextName) + '.txt'

        res_s.append(res_f[fileName])
    except ValueError:
        break

print(res_s)

for el in res_s:
    if ((el != '') and (el != ' ') and (el != '*') and (el != '\n')):
        res_t.append(el)

print(res_t)