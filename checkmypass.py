from requestapidata import request_api_data
from passwordleaks import get_password_leaks_count
import hashlib
import sys


def pwned_api_check(password):
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count}...you should change your password asap!')
        else:
            print(f'{password} was not found. You\'re good!')
        return 'done'


main(sys.argv[1:])
