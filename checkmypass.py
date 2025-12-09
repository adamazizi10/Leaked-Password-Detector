from requestapidata import request_api_data
from passwordleaks import count_password_leaks
import hashlib
import sys


def pwned_api_check(password):
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return count_password_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should probably change your password!')
        else:
            print(f'{password} was not found. You\'re good!')
        return 'done'


main(sys.argv[1:])
