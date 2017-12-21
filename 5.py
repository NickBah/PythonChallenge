from urllib import request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
res = []
for i in range(401):
    with request.urlopen(url) as x:
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+x.read(300).decode('utf-8').split(' ')[-1]
        if x.read(300).decode('utf-8').split(' ')[-1].isalpha():
            res.append(x.read(300).decode('utf-8').split(' ')[-1])
        print(i, url)
print(res)