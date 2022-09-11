import requests
import hashlib

def api_response(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the api and try again')
    return res

def password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)

def pwnd_check(password):
    password = str(password)
    sh1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firs5_char, tail = sh1pass[:5], sh1pass[5:]
    response = api_response(firs5_char)
    return password_leaks_count(response, tail)

pwnd_check(123)