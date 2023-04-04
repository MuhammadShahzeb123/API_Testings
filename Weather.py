import requests
import json

location = ['sargodha', 'islamabad', 'karachi', 'lahore']
url = f'http://api.weatherapi.com/v1/current.json?key=b22d203be7074b00bb865621232603&q={location[0]}'

response = requests.get(url)

if response.status_code == 200:
    content = response.content
    dic = json.loads(content)
    if __name__ == '__main__':
        print(dic['current']['temp_c'])

else:
    print('Failed to retrieve content')