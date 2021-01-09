import requests


datetime = input('Enter current date and time in YYYY/MM/DD H:M:S format : ')

url = f'http://127.0.0.1:8000/{datetime}/checkstatus'

response = requests.get(url=url)

data = response.json()

print(data['status'])

url='http://127.0.0.1:8000/ping/'

response1 = requests.get(url=url)

server_status = response.json()

print(server_status)
print(server_status)