'''
Project: Binlist.net Python 3
Author: Göktürk Enez
'''

from urllib.request import Request, urlopen

binNumbers = ["511583", "432284", "547234", "417715"]
for binNumber in binNumbers:
    print(binNumber)
    url = 'https://lookup.binlist.net/'+binNumber
    request = Request(url)
    response = urlopen(request).read().decode()
    print(response)

