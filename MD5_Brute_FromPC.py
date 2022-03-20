from urllib.request import urlopen
import hashlib
from colorama import init
from termcolor import colored
init(convert=True)

#Open from file
def tryOpen(wordlist1):
    global pass_file
    try:
        pass_file = open(wordlist1, "r")
    except:
        print("[!!] No Such File At That Path!")
        quit()

wordlist2 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist1 = input("[*] Enter Path To The Password File: ")

tryOpen(wordlist1)

for word in pass_file:
    print(colored("[-] Trying: " + word.strip("\n", 'red')))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5digest == pass_hash:
        print(colored("[+] Password Found: " + word, 'green'))


for password in wordlist2.split('\n'):
    print(colored("[-] Trying: " + word.strip("\n", 'red')))

    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    #hashguess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    if md5digest == pass_hash:
        print(colored("[+] The Password is: " + str(password), 'green'))
        quit()

print("[!!] Password Not In List!")

