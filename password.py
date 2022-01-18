#!/bin/python3

import hashlib,argparse,getpass #Importing modules necessary [hashlib for genereting hash],[argparse for getting input from command], [get pass for getting input secretly] 

def sha(string): #A function to take a string and convert it into sha256
    return hashlib.sha256(string.encode()).hexdigest() 

def take_input(): #A function to take input of passphrase from user
    parse = argparse.ArgumentParser()
    parse.add_argument("-p","--passphrase")
    options = parse.parse_args()
    if options.passphrase is None:
        passphrase= getpass.getpass(prompt="")
        return passphrase+"."#To identify weather passphrase is given by which process, while . is not the charecters involved in special_chars down
    else:
        return options.passphrase
        
def return_string_from_sha(sha): #A function to give a number between 0 to 26 from inputed sha256 hash
    supporter = []
    to_return = 0
    for lota in range(0,13):
        letter = sha[lota*2]
        if letter.isdigit():
            if int(letter)<4:
                supporter.append(0)
            else:
                supporter.append(1)
        else:
            supporter.append(2)
    for nums in supporter:
        to_return = to_return + nums
    return to_return

def return_password(passphrase,length): #A function to return password from given passphrase with specific length
    small_chars = "abcdefghijklmnopqrstuvwxyza"
    big_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"#There are 27 letters because return_string_from_sha will give maximum value 26 and 26 will give 27th letter
    special_chars = "!@#$%^&*()_+=-[{~|;:?/<>}],"
    nums = "123456789098765432123456789"
    password = []
    encrypt = sha(passphrase)
    for tola in range(0,length):
        letter = encrypt[tola]
        if letter.isdigit():
            if int(letter)<4:
                password.append(small_chars[return_string_from_sha(sha(str(tola+1)+letter+str(length*2)))])
            else:
                password.append(big_chars[return_string_from_sha(sha(str(length+3)+letter+str(tola*4)))])
        elif letter == "a" or letter == "b" or letter == "c":
            password.append(special_chars[return_string_from_sha(sha(str(tola+5)+letter+str(length*6)))])
        else:
            password.append(nums[return_string_from_sha(sha(str(length+7)+letter+str(tola*8)))])
    return "".join(password)

phrase = take_input()
length = 21 #can change length of password (BETWEEN 1-32)

if phrase[-1]==".": #To paste the generated password in the clipboard if passphrase is given secretly
    phrase = phrase[0:-1]
    import pyperclip 
    pyperclip.copy(return_password(phrase,length))
else:
    print(f"\033[0;31m\t{return_password(phrase,length)}") #To print generated password in screen if passphrase is given openly  

