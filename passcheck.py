import requests
import hashlib

def api_response(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the api and try again')
    return res

def pwnd_check(password):
    password = str(password)
    sh1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sh1pass

pwnd_check(123)