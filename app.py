import requests

#getting date and time
datetime = input('Enter current date and time in YYYY/MM/DD H:M:S format : ')

#storing url
url = f'http://127.0.0.1:8000/{datetime}/checkstatus'

#sending get request
response = requests.get(url=url)

#converting the response into json
data = response.json()

#printing the response
print(data['status'])

##checking whether server is active
url='http://127.0.0.1:8000/ping/'

#sending get request
response1 = requests.get(url=url)

#converting the response into json
server_status = response.json()

print(server_status)
print(server_status)
