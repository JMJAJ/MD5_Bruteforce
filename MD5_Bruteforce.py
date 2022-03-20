from urllib.request import urlopen
import hashlib
from colorama import init
from termcolor import colored
init(convert=True)

wordlist2 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

pass_hash = input("[*] Enter MD5 Hash Value: ")

for password in wordlist2.split('\n'):
    enc_wrd = password.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if md5digest == pass_hash:
        print(colored("[+] The Password is: " + str(password), 'green'))
        #quit()
        break
    else:
        print(colored("[-] Password quess " + str(password) + " does not match, trying again...", 'red'))


print("[!!] Password Not In List!")

#2d50fbc104409eb0b9a17413026ac06f