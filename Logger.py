#!/usr/bin/python3

import requests
login_url = 'Your_URL'
login_data = {
    'mode' : 191,
    'username': 'Your_Username',
    'password': 'Your_Password'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

session = requests.Session()

try:
    response = session.post(login_url, data=login_data, headers=headers, timeout = 5)
    
    if response.status_code == 200:
        print('Login successful!')
    else:
        print('Login failed.')
except requests.exceptions.RequestException as e:
    print('Error:', e)
