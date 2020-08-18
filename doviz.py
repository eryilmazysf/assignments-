import requests
url='http://data.fixer.io/api/latest?access_key=9908004f3a7b93a4f3d82adee0346d6f'
response=requests.get(url)
json=response.json()
print('USD TO TRY:',json['rates']['TRY']/json['rates']['USD'])