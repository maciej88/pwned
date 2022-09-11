import requests
import hashlib
import sys

def api_response(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the api and try again')
    return res

def password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwnd_check(password):
    password = str(password)
    sh1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firs5_char, tail = sh1pass[:5], sh1pass[5:]
    response = api_response(firs5_char)
    return password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwnd_check(password)
        if count:
            print(f'{password} was FOUND {count} times, change it!')
        else:
            print(f'{password}, NOT FOUND!')
    return '==end of checking=='

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))