passwords_file='passwords.txt'
password_list= open(f'{passwords_file}',"r")
numbers='12345'

for password in password_list:
    pwd=password.strip()
    if len(pwd)<8:
        pwd= pwd + numbers[0:1+8-len(password)]
    else:
        pwd= pwd

    print(pwd)