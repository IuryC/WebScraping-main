import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status code: ', response.status_code)
print('Header: ')
print(response.headers)
print('Content')
print(response.content)