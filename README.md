
#  Generate Random Password with Passphrase

This is a python code to generate strong Password from given pass phrase. A slightly Different Passphrase will give completly different Password. A same Passphrase will always give a same Password.

If it is hard to remember a strong password and weak password will be cracked easily so it can generate a strong password from easy passphrase so passphrase will be easily can be remembered.
## How to use
To use first of all get this code to get code you can clone this repo by command:
    
    git clone https://github.com/hailzen/create_password

Then change your working directory by typing 

    cd create_password


There are two ways to generate password from it 


### First (open) 

    python password.py -p passphrase 
passphrase is actual passphrase

The **Output** will be password. For eg:

    python password.py -p secret

        l{=Qo9QnR(r5+o4qP+2pk
Then you can copy and paste 

### Second (secret) {Reccomended}
Type

    python password.py
**Then blank screen appears write passphrase there it wont show passphrase beacause it is secret**

After you enter your pass phrase click enter then password will be copied in your clipboard then you can paste it by *Ctrl+v*
## At Last

Defult length of password is 21 if you want to change it then with any text editor open password.py and in line *55* there is :

    length = 21
To change length change value between **1-31**


for eg to get password of length 26 change will look like

    length = 26

