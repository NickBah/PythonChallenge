from collections import Counter
import zipfile
path = 'channel.zip'
name='90052.txt'
tmp = []
res = []
try:
    myzip = zipfile.ZipFile(path, 'r')
    list = myzip.namelist()
    for i in list:
        res.append(str(myzip.getinfo(i).comment, 'utf-8'))
except:
    None

print(Counter(res))